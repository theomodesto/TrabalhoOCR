# -*- coding: utf-8 -*-
from ORC.TesseractOCR import pytesseract
from ProcessaImage.LimpaImagem import processe_img
from PIL import Image
import serial

ser = serial.Serial('/dev/ttyUSB0')

img = Image.open('/home/henrique/Documentos/TrabalhoOCR/plate.jpg') 

imgProc = processe_img(img)

text = pytesseract(img)

PLACA_AUTENTICADA = 'BEE4R22'

if(PLACA_AUTENTICADA == text):
    ser.write(b'1')
else:
    ser.write(b'0')