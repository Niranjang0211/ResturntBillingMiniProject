import glob
import json
import os
import time

import openpyxl
#import folder
import requests

upload_url = "http://172.16.2.40:5000/upload_file"
#file_path = "C:\\Users\\surya.n\\Downloads\\ImageRepository\\Images\\Reference Images\\baj links.png"

folder = r"D:\YOLO Mobile 2.2\Nagesh Images\Set2"
file_paths = glob.glob(os.path.join(folder, '**'), recursive=True)
file_paths = [path for path in file_paths if os.path.isfile(path) and (path.endswith(".jpg") or path.endswith(".PNG")or path.endswith(".png"))]
#print(file_paths)


workbook = openpyxl.Workbook()
sheet = workbook.active
colval=2
for i in file_paths:
    with open(i, 'rb') as file:
        # Create a dictionary for the file upload
        files = {'file': (file.name, file)}
        # Headers can include form data or other required headers
        uploadfile_data = {
            "orgid": "52468647263",
            "tokenid": "546img8",
            "service": "Image"
        }
        # Make the POST request with the file and headers
        response = requests.post(upload_url, files=files, data=uploadfile_data)
        uploaded_image_name = response.json()["result"]
        image_identifier_url = "http://172.16.2.40:5000/imageclassfinder"
        classifer_data = {
            "orgid": "52468647263",
            "tokenid": "546img8",
            "service": "Image",
            "imagename": uploaded_image_name
        }
        identifier_response = requests.post(image_identifier_url, files=files, data=classifer_data)
        time.sleep(2)


        sheet['A1'] = 'Image Name'
        sheet['B1'] = 'Image Class'
        sheet[f'A{colval}'] = file.name.split("\\")[-1]
        sheet[f'B{colval}'] = identifier_response.json()["result"]
        colval+=1

workbook.save(r"D:\YOLO Mobile 2.2\Nagesh Images\Set2\image_data.xlsx")


