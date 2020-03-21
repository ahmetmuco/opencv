# -*- coding: utf-8 -*-
import numpy as np
import cv2

"""
@author = 'Ahmet Mucahit Tarakci'
"""

cap = cv2.VideoCapture('nivea.mp4')

while True:
    # Take each frame
    ret,frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  # HSV renk uzayına dönüştürüldü.

    # define range of blue color in HSV
    lower_blue = np.array([90,50,50])  # H,S,V değerleri
    upper_blue = np.array([130,255,255])  # Bulmak istediğimiz rengin H değer aralığını ve-
    # diğer değerleri numpy dizisi olarak tutuyoruz.

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv,lower_blue,upper_blue)  # Aralık değerlerini maskeye veriyoruz.

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame,frame,mask=mask)

    # Smoothing
    kernel = np.ones((5,5),dtype=np.float32) / 25  # sondaki 25, kernelin boyutları carpımı. (5,5) ise sonu 25 gibi.
    smoothed = cv2.filter2D(result,-1,kernel)

    # Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(result,(5,5),0)  # ilk parametre uygulanacak görüntü, ikinci parametre kernelsize

    # Median
    median = cv2.medianBlur(result,5)  # ilk parametre uygulanacak görüntü, ikinci parametre kernelsize

    # Bilateral Filtering
    bilateral = cv2.bilateralFilter(result,5,75,75)

    cv2.imshow('Orijinal Video',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    cv2.imshow('hsv',hsv)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('gaussian_blur',gaussian_blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)

    if cv2.waitKey(35) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
