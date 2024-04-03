from PIL import Image
import requests
import json

def get_txt_from_img(img_name):

    headers = {
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
    }

    files = {
       'file': open(img_name, 'rb'),
    }

    response = requests.post('http://54.147.188.222:8090/detect_text', headers=headers, files=files)

    arabic_text = json.loads(response.text)["result"]
    decoded_text = bytes(arabic_text, 'utf-8').decode('unicode_escape')

    return decoded_text
