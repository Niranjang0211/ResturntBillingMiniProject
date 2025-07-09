import glob
import json
import os
import time
import folder
import requests

url = "http://172.16.2.40:8000/upload_file"
#file_path = "C:\\Users\\surya.n\\Downloads\\ImageRepository\\Images\\Reference Images\\baj links.png"

folder = r"D:\2nd Time Stub verification\TitleVerification"

file_paths = glob.glob(os.path.join(folder, '**'), recursive=True)
# Filter out directories
file_paths = [path for path in file_paths if os.path.isfile(path)]
print(file_paths)

for i in file_paths:
    with open(i, 'rb') as file:
        # Create a dictionary for the file upload
        files = {'file': (file.name, file)}

        # Headers can include form data or other required headers
        data = {
            "orgid": "52468647263",
            "tokenid": "546img8",
            "service": "Image"
        }
        # Make the POST request with the file and headers
        response = requests.post(url, files=files, data=data)

        # Check the response status
        if response.status_code == 200:
            print('File uploaded successfully!')
            print('Response:', json.dumps(response.json()))
        else:
            print('Failed to upload file. Status code:', response.status_code)
            print('Response:', response.text)
            #break

        fileName = response.json()["result"]
        print(fileName)
        time.sleep(3)
        detectControl = "http://172.16.2.40:8000/detectcontrols"
        detectControlBody = {
            "imagename": fileName,
            "orgid": "52468647263",
            "tokenid": "546img8",
            "service": "Image"
        }
        response = requests.post(detectControl, data=detectControlBody)
        print(response.json())
        if response.status_code == 200:
            jsonfilename = (i.split('\\')[-1]).split('.')[0] + ".json"
            save_path = r"D:\2nd Time Stub verification\TitleVerification\Json"
            file_path = os.path.join(save_path, jsonfilename)
            try:
                response_data = response.json()
                with open(file_path, 'w') as file:
                    json.dump(response_data, file, indent=4)
                print('Response has been saved to response.json')
            except ValueError:
                print('Response content is not valid JSON')
            else:
                print("DetectControlsFailed for :",jsonfilename)

        # folder = "C:\\Users\\surya.n\\Downloads\\ImageRepository\\Images\Reference Images"
        # file_paths = glob.glob(os.path.join(folder, '**'), recursive=True)
        # # Filter out directories
        # file_paths = [path for path in file_paths if os.path.isfile(path)]
        # print(file_paths)
        #print((i.split('\\')[-1]).split('.')[0])
print("All images Json generated successfully....")