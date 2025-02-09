import os
os.system('pip install gutenbergpy')
os.system('pip install requests')

import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
from gutenbergpy.textget import get_text_by_id


def remove_funny_tokens(text):
    tokens = text.split()
    sample = ' '.join(' '.join(tokens).replace('xe2x80x9c', ' ').replace('xe2x80x9d', ' ')\
                                      .replace('xe2x80x94', ' ').replace('xe2x80x99', "'")\
                                      .replace('xe2x80x98', "'").split())
    return sample


def clean_text(text):
    cleaned_listed_text = []
    listed_text = list(text)

    for iter in range(len(listed_text) - 1):
        if (listed_text[iter] == '\\' and listed_text[iter + 1] == 'n') or \
            (listed_text[iter] == 'n' and listed_text[iter - 1] == '\\'):
            continue
        elif listed_text[iter] == '\\' and listed_text[iter + 1] == 'r' or \
            (listed_text[iter] == 'r' and listed_text[iter - 1] == '\\'):
            continue
        elif listed_text[iter] == '\\' and listed_text[iter + 1] == 't' or \
            (listed_text[iter] == 't' and listed_text[iter - 1] == '\\'):
            continue
        elif listed_text[iter] == '\\':
            continue
        else:
            cleaned_listed_text.append(listed_text[iter])

    cleaned_text = ''.join([str(char) for char in cleaned_listed_text])
    cleaned_text = remove_funny_tokens(cleaned_text)

    return ''.join(cleaned_text)

df_metadata = pd.read_csv('gutenberg_metadata.csv')

data = {'Author': [], 'Title': [], 'Link': [], 'ID': [], 'Bookshelf': [], 'Text': []}

for key, row in df_metadata.iterrows():
    data['Author'].append(row['Author'])
    data['Title'].append(row['Title'])
    data['Link'].append(row['Link'])

    book_id = int(row['Link'].split('/')[-1])
    data['ID'].append(book_id)
    data['Bookshelf'].append(row['Bookshelf'])

    text = np.nan
    try:
        text = get_text_by_id(book_id).decode('utf-8')
        text = ' '.join(' '.join(' '.join(text.split('\n')).split('\t')).split('\r'))
        text = ' '.join(text.split())
        text = clean_text(str(text))
    except Exception as e:
        print(f"Couldn't acquire text for {row['Title']} with ID {book_id}. Link: {row['Link']}. Error: {e}")
            
    try:
        data['Text'].append(' '.join(text.split(' ')))
    except Exception as e:
        data['Text'].append(None)
        print(f"Couldn't save data for {row['Title']} with ID {book_id}. Link: {row['Link']}. Error: {e}")

df_data = pd.DataFrame(data, columns=['Title', 'Author', 'Link', 'ID', 'Bookshelf', 'Text'])

df_data.to_csv('/content/gutenberg_data.csv', index=False)

