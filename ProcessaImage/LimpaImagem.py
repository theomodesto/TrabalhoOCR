import cv2
import numpy as np

from PIL import Image, ImageEnhance, ImageFilter
from PIL.ImageOps import grayscale


def processe_img(img):

    img.save('antes.jpg')

    '''Converte para cinza'''
    img = grayscale(img)

    '''Reduz ruido'''
    img = img.filter(ImageFilter.MedianFilter())

    '''Aumenta o contraste'''
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)

    '''Converte a image para matrix'''
    img = np.array(img)

    '''Converte para binario a image'''
    _, binimg = cv2.threshold(np.asarray(img).astype(np.uint8), 60, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # binimg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 127, 1)

    '''Kernel'''
    # rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))

    '''Aumenta o tracado'''
    # imgTracado = cv2.dilate(binimg, rectKernel, iterations=1)

    '''Reduz o tracado'''
    # imgTracado = cv2.erode(binimg, rectKernel, iterations=1)

    img = Image.fromarray(binimg)

    img.save('depois.jpg')

    return img