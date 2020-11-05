from ORC.TesseractOCR import pytesseract
from ProcessaImage.LimpaImagem import processe_img
from PIL import Image

img = Image.open('/home/theo/Documents/UP/TOPICOS_ESPECIAIS/python-ocr-arduino/input/oPlate_2.jpg') 

imgProc = processe_img(img)

text = pytesseract(img)

print("TEXT", text)