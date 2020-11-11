import cv2
import numpy as np
from imutils import contours

image = cv2.imread('input/Placa.jpg')
mask = np.zeros(image.shape, dtype=np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
(cnts, _) = contours.sort_contours(cnts, method="left-to-right")
ROI_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    if area < 3000 and area > 1500:
        x,y,w,h = cv2.boundingRect(c)
        ROI = 255 - thresh[y:y+h, x:x+w]
        cv2.drawContours(mask, [c], -1, (255,255,255), -1)
        cv2.imwrite('ROIs/ROI_{}.png'.format(ROI_number), ROI)
        ROI_number += 1

cv2.imshow('mask', mask)
cv2.imshow('thresh', thresh)
cv2.waitKey()