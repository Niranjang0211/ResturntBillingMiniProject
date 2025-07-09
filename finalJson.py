import json
import re
import os
import glob
from collections import Counter
import openpyxl
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
folder = r"D:\YOLO Mobile 2.2\mobile-001\mobile\images json"
words_to_count = [
    "Spin Box", "Check Box", "Combo Box", "Push Button", "Radio Button", "Text Box", "List Box", "Tree", "Grid", "Page Tab",
    "Menu bar", "Scroll bar", "Title bar", "Title bar - Close button only", "Title bar - Minimize button only",
    "Title bar - Restore button only", "Title bar - With all Button", "Menu Items", "Tool bar", "Link", "Label", "Checkbox with label",
    "Radio Button with label", "Calendar Control", "Cursor button (mouse)", "Status bar", "Horizontal scroll bar",
    "Vertical scroll bar", "Title"
]

# Get list of all JSON files in the folder
text_files = glob.glob(os.path.join(folder, '*.json'))

# Initialize a dictionary to store word counts for each file
file_word_counts = {}

# Process each JSON file in the folder
for file_path in text_files:
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            # Convert JSON data to a flat string
            flat_string = json_to_string(data)

            # Initialize Counter for the current file
            word_counts = Counter()

            # Count occurrences of each word in the current file
            for word in words_to_count:
                pattern = re.escape(word)
                matches = re.findall(pattern, flat_string)
                word_counts[word] = len(matches)

            # Store the counts in the dictionary with the file name as the key
            file_word_counts[os.path.basename(file_path)] = word_counts
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")

# Print the word counts for each file
for file_name, counts in file_word_counts.items():
    print(f"File: {file_name}")
    for word, count in counts.items():
        print(f"  {word} : {count}")
    print()



