import csv
import re

file_list_csv = "file_list.csv"  # Original file list with exact names
processed_data_csv = "processed_file_data.csv"  # Gemini-enhanced data
output_csv = "merged_file_data.csv"  # Final merged file

def clean_text(text):
    text = re.sub(r"\*\*|\*", "", text)
    text = re.sub(r"(?i)unknown era", "Era not specified", text)
    text = text.strip().capitalize()
    if text and not text.endswith("."):
        text += "."
    return text

file_list_dict = {}
with open(file_list_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        if len(row) >= 3:
            exact_name, proper_name, file_path = row[:3]
            file_list_dict[proper_name] = [exact_name, file_path]

merged_data = []
with open(processed_data_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        if len(row) >= 3:
            proper_name = row[0].strip()
            description = clean_text(row[1])
            timeline = clean_text(row[2])

            
            exact_name, file_path = file_list_dict.get(proper_name, ["Unknown", "Unknown"])

            merged_data.append([exact_name, proper_name, description, timeline, file_path])

with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Exact File Name", "Proper Name", "Description", "Timeline/Era", "File Path"])  # Header
    writer.writerows(merged_data)

print(f"Merged and cleaned file saved as {output_csv}")
