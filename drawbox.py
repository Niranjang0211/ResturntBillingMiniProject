import cv2
import pandas as pd
import os
from PIL import Image
import json
from datetime import datetime


class drawbox():

  def __init__(self):
    pass

  def drawboxes(self, imgpath, data, output_path, controls):
    try:
      
      with open(data, 'rb') as f:
        dat = f.read()
      
      result = json.loads(dat) 
      
      model_1 = result['model_1']
      model_5 = result['model_5']

      response = self.draw("model_1", output_path, imgpath, model_1, controls)
      response1 = self.draw("model_5", output_path, imgpath, model_5, controls)
      if response == False or model_1response1 == False:
        raise Exception(f" status: {response}; model_5 status: {response1}")

      return "File saved!"
    except Exception as e:
      print("Error: ", e)
      return False
      
      
  def draw(self, modelname, output_path, imgpath, result, controls):
    conf = result['conf']
    ctrlist = [str.strip(ctrls) for ctrls in controls.split("|")]
    cls = result['cls']
    boxes = result['xyxy']
    im_bgr = cv2.imread(imgpath)
    
    for i, confvalues in enumerate(conf):
      if str.strip(controls) != "*" and  str(int(cls[i][0])) not in ctrlist:
        print("skipping: ", cls[i][0])
        continue
            
        
      x1, y1, x2, y2 = boxes[i]
      thickness = 2
      cls_id = str(int(cls[i][0]))
      color = self.getcolor(cls_id)
      cv2.rectangle(im_bgr, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
      cv2.rectangle(im_bgr, (int(x1), int(y1)), (int(x1)+25, int(y1)+20), (0,0,0), -1)
      cv2.putText(im_bgr, cls_id, (int(x1), int(y1) +15 ), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (225,225,225), 2)
      #cv2.putText(im_bgr, cls_id, (int(x1), int(y1) +15 ), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
      
  
    #cv2_imshow(im_bgr)
        
    im_rgb = Image.fromarray(im_bgr[..., ::-1]) 
    
    timestamp = datetime.now().strftime("%d-%m-%y_%H%M%S%f")
    name = os.path.basename(imgpath)
    filename = f'{modelname}_{name}'
    im_rgb.save(f'{output_path}/{timestamp}_{filename}')
    return True

  def getcolor(self, cls):
    colordict = {
        '0': (0,255,0),
        '1': (255,0,0),
        '2': (0,0,255),
        '3': (255,255,0),
        '4': (0,255,255),
        '5': (255,0,255),
        '6': (65,105,225),
        '7': (128,128,0),
        '8': (0,128,0),
        '9': (128,0,128),
        '10': (0,128,128),
        '11': (0,0,128),
        '12': (165,42,42),
        '13': (255,127,80),
        '14': (250,128,114),
        '15': (255,160,122),
        '16': (255,140,0),
        '17': (218,165,32), 
        '18': (189,183,107),
        '19': (0,100,0),
        '20': (34,139,34),
        '21': (152,251,152),
        '22': (143,188,143),
        '23': (139,0,139),
        '24': (100,149,237),
        '25': (135,206,235),
        '26': (138,43,226), 
        '27': (255,20,147), 
        '28': (218,165,32)
    }

    return colordict[str(cls)]

if __name__ == '__main__':
  
  draw = drawbox()
  #ctrls = "*"
  ctrls = "*"

  '''
  ## To match image name and json file name from a folder and send to model: 
  
  imagepaths = os.listdir(r'D:\DDownloads\drawbox\ORG IMAGES')
  jsonpaths = os.listdir(r'D:\DDownloads\drawbox\Json Path')
  outputpath = r'D:\DDownloads\drawbox\Boxed_Images_new'
  os.makedirs(outputpath, exist_ok = True)
  json_base_filenames = [filename.split('.',1)[0] for filename in jsonpaths]
  image_base_filenames = [filename.split('.',1)[0] for filename in imagepaths]
  matching_image_filenames = []
  nonmatching = []
  for image_filename in json_base_filenames:
    if image_filename in image_base_filenames:
        matching_image_filenames.append(image_filename)
    else:
        nonmatching.append(image_filename)
        print(image_filename)
  #matching_image_filenames = [image_filename for image_filename in image_base_filenames if image_filename in json_base_filenames]
  
  print("non matching: ", len(nonmatching))
  print("images: ",len(imagepaths))
  print("json: ",len(jsonpaths))
  print("total: ",len(matching_image_filenames))
  
  for names in matching_image_filenames:
    
    imgpath = os.path.join(r'D:\DDownloads\drawbox\ORG IMAGES',[filename for filename in imagepaths if filename.startswith(names+".")][0])
    jsonres = os.path.join(r'D:\DDownloads\drawbox\Json Path',[filename for filename in jsonpaths if filename.startswith(names+".")][0])
    print(draw.drawboxes(imgpath, jsonres, outputpath, ctrls))
  
  
  
  print(nonmatching)
  '''
  

  ## To get imagepath and json filepath from excel to feed to model:
  
  draw = drawbox()
  excel_path = r"D:\YOLO 2.0\Excel.xlsx"
  outputpath = r"D:\YOLO 2.0\Output"
  df = pd.read_excel(excel_path)
  imagepath = [path for path in df['imagepath']]
  jsonpath = [path for path in df['jsonpath']]
  for i,img in enumerate(imagepath):
    imgpath = imagepath[i]
    jsonres = jsonpath[i]
    print(draw.drawboxes(imgpath, jsonres, outputpath, ctrls))

print("All images predicted successfully....")