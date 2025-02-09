import csv
import google.generativeai as genai

GEMINI_API_KEY = "--" #Anyone can enter there API Key while Running
genai.configure(api_key=GEMINI_API_KEY)

input_csv = "file_list.csv" 
output_csv = "processed_file_data.csv"

proper_names = []
with open(input_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        if len(row) > 1:  
            proper_names.append(row[1])

def get_gemini_info(name):
    prompt = f"""Provide a short description of '{name}' and its historical timeline. 
                 Mention which historical era or period it belongs to. 
                 Even if the timeline is not certain, make an educated guess."""
    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
        text = response.text.strip()

        if "Timeline:" in text:
            desc, timeline = text.split("Timeline:", 1)
        else:
            desc, timeline = text, "Unknown Era"

        return desc.strip(), timeline.strip()
    except Exception as e:
        return "Error fetching data", "Unknown Era"

processed_data = []
for name in proper_names:
    description, timeline = get_gemini_info(name)
    processed_data.append([name, description, timeline])

with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Proper Name", "Description", "Timeline"])  # Header
    writer.writerows(processed_data)

print(f"Processed data saved in {output_csv}")
