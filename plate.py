import cv2
#############################################
frameHeight = 480
frameWidth = 640
nPlateCascade = cv2.CascadeClassifier("/home/theo/Documents/UP/TOPICOS_ESPECIAIS/python-ocr-arduino/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255, 0, 255)
###############################################
img = cv2.imread('/home/theo/Documents/UP/TOPICOS_ESPECIAIS/python-ocr-arduino/input/oPlate_2.jpg')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img", imgGray)
cv2.waitKey(1500)

numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
for (x, y, w, h) in numberPlates:
    area = w * h
    if area > minArea:
        cv2.rectangle(img,
                      (x, y),
                      (x + w, y + h),
                      (255, 0, 255), 2)

        cv2.putText(img, "Number Plate", (x, y - 5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

        imgRoi = img[y:y + h, x:x + w]

        cv2.imshow("ROI", imgRoi)
        cv2.waitKey(1500)

        cv2.imwrite("NoPlate_teste.jpg", imgRoi)
