#Script for extreacting the keywords

import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer

def read_files_from_folder(folder_path):
    texts = []
    file_names = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                texts.append(file.read())
                file_names.append(file_name)
    return texts, file_names

def extract_keywords(texts, top_n=10):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    keywords = []

    for row in X:
        sorted_items = sorted(zip(row.data, row.indices), reverse=True)
        keywords.append([feature_names[idx] for _, idx in sorted_items[:top_n]])

    return keywords

def save_keywords_to_json(keywords, file_names, output_file):
    data = {file_name: keyword_list for file_name, keyword_list in zip(file_names, keywords)}
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"JSON file '{output_file}' created with keywords from {len(file_names)} files.")

if __name__ == "__main__":
    folder_path = "/Users/mmadhusudan/Desktop/MyFiles/Gutenberg_Books"  # Replace with the path to your folder containing text files
    output_file = "keywords_output.json"  # The name of the JSON file to be created

    texts, file_names = read_files_from_folder(folder_path)
    keywords = extract_keywords(texts)
    save_keywords_to_json(keywords, file_names, output_file)
