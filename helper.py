from PIL import Image
import pytesseract



def get_txt_from_img(img_name):
    return pytesseract.image_to_string(Image.open(img_name))
