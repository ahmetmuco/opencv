# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Üzerinde çalışılacak video değişkene atandı.
cap = cv2.VideoCapture('nivea.mp4')

while True:
    # Take each frame
    ret,frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  # HSV renk uzayına dönüştürüldü.

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])  # H,S,V değerleri
    upper_blue = np.array([130,255,255])  # Bulmak istediğimiz rengin H değer aralığını ve-
    # diğer değerleri numpy dizisi olarak tutuyoruz.

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv,lower_blue,upper_blue)  # Aralık değerlerini maskeye veriyoruz.

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Orijinal Video',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    cv2.imshow('hsv',hsv)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
