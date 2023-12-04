import cv2
import numpy as np
import utils as u

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)


cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("Video/2023-10-24-155544.webm")
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict)
    list_posAruco = u.aruco_display(corners,ids, 0,img)
    # image_with_markers = cv2.aruco.drawDetectedMarkers(img.copy(), corners, ids)

    # print(corners)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()