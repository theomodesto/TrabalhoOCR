import pytesseract as ocr

'''
:param img object do Image do PIL 
:return string com dados da image 
'''
def pytesseract(img):
    text = ocr.image_to_string(img)
    text = text.replace("Lee [Ss", "")
    text = text.replace("Atomoves Carinnies, Onbus ¢ Rebogues", "")
    text = text.replace(" ", "")
    text = text.replace(":", "")
    text = text.strip()

    return text