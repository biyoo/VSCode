import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'

img = Image.open('PythonTest/1.jpg')
text = pytesseract.image_to_string(img, lang='kor')
print(text)