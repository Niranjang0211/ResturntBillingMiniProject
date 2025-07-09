import json
import re
import os
import glob
from collections import Counter
import pandas as pd

# Function to recursively convert JSON to a flat string
def json_to_string(data):
    if isinstance(data, dict):
        return ' '.join([json_to_string(value) for value in data.values()])
    elif isinstance(data, list):
        return ' '.join([json_to_string(element) for element in data])
    else:
        return str(data)

# Path to your folder containing JSON files
folder = r"C:\Users\niranjan.m\Downloads\ORG IMAGES-20250505T084626Z-1-001\ORG IMAGES"
words_to_count = [
     "Spin Box", "Check Box", "Combo Box", "Push Button", "Radio Button", "Text Box", "List Box", "Tree", "Grid", "Page Tab",
    "Menu Bar", "Scroll bar", "Title bar", "TB - Close button", "TB - Minimize button",
    "TB - Restore button", "Title bar - With all Button", "Menu Items", "Tool bar", "Link", "Label", "Checkbox with label",
    "Radio Button with label", "Calentar Control", "Cursor button (mouse)", "Status Bar", "Horizontal Scroll Bar",
    "Vertical Scroll Bar","Title"
]

# Get list of all JSON files in the folder
text_files = glob.glob(os.path.join(folder, '*_yolo5.txt'))

# Initialize a list to store all records
records = []

# Process each JSON file in the folder
for file_path in text_files:
    with open(file_path, 'r') as file:
        try:
            data = file.read()
            # Convert JSON data to a flat string
            flat_string = json_to_string(data)

            # Initialize Counter for the current file
            word_counts = Counter()

            # Count occurrences of each word in the current file
            for word in words_to_count:
                pattern = re.escape(word)
                matches = re.findall(pattern, flat_string)
                count = len(matches)

                #if word == "Push Button":
                 #   count -= 22


                # Append each count as a record
                records.append({
                    "File Name": os.path.basename(file_path),
                    "Controls": word,
                    "Total Controls": " ",
                    "Identified Controls": count,
                    "Wrong Identified":" "
                })
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")

# Convert the list of records to a DataFrame
df = pd.DataFrame(records)

# Path to the output Excel file
output_excel_file = r"C:\Users\niranjan.m\Downloads\ORG IMAGES-20250505T084626Z-1-001\ORG IMAGES.xlsx"

# Write the DataFrame to an Excel file
df.to_excel(output_excel_file, index=False)

print(f"Word counts successfully written to {output_excel_file}")
