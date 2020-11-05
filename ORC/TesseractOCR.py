import pytesseract as ocr

'''
:param img object do Image do PIL 
:return string com dados da image 
'''
def pytesseract(img):
    text = ocr.image_to_string(img)
    # pdf = ocr.image_to_pdf_or_hocr(img, lang='por', extension='pdf')
    # hocr = ocr.image_to_pdf_or_hocr(img, lang='por', extension='hocr')
    return text