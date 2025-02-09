import os
import csv

folder_path = "/Users/mmadhusudan/Desktop/MyProject/My3DModels"

output_csv = "file_list.csv"


def format_filename(filename):
    name, _ = os.path.splitext(filename)  # Remove extension
    name = name.replace("_", " ").replace("-", " ").title()  # Replace _ and - with spaces and capitalize
    return name


file_data = []
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        formatted_name = format_filename(file)
        file_data.append([file, formatted_name, file_path])


with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Exact File Name", "Formatted Name", "File Path"])  # Header
    writer.writerows(file_data)

print(f"File list saved in {output_csv}")
