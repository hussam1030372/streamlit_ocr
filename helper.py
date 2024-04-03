from PIL import Image
import requests

def get_txt_from_img(img_name):

    headers = {
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
    }

    files = {
       'file': Image.open(img_name),
    }

    response = requests.post('http://54.147.188.222:8090/detect_text', headers=headers, files=files)

    return response
