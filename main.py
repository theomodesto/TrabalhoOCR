from ORC.TesseractOCR import pytesseract
from ProcessaImage.LimpaImagem import processe_img
from PIL import Image

img = Image.open('/home/henrique/Documentos/TrabalhoOCR/plate.jpg') 

imgProc = processe_img(img)

text = pytesseract(img)

PLACA_AUTENTICADA = 'BEE4R22'

if(PLACA_AUTENTICADA == text):
    print('Placa Autorizada')
else:
    print('Placa não autorizada')