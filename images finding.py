import pandas as pd
import shutil
import os

# Set your paths here
excel_path = r"C:\Users\niranjan.m\Desktop\images.xlsx"
source_folder =r"D:\YOLO Mobile 2.2\For Automation\UnTrained Images Desktop\ORG"
destination_folder = r"D:\YOLO Mobile 2.2\For Automation\UnTrained Images Desktop\ORG\Final Images"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Read the Excel file (assumes image names are in column 'filename')
df = pd.read_excel(excel_path)

# Loop through each file name and copy it
for image_name in df['filename']:
    src_path = os.path.join(source_folder, image_name)
    dest_path = os.path.join(destination_folder, image_name)

    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        print(f"Copied: {image_name}")
    else:
        print(f"Not found: {image_name}")
