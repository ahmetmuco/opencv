# -*- coding: utf-8 -*-
import numpy as np
import cv2

"""
@author = 'Ahmet Mucahit Tarakci'
"""

cap = cv2.VideoCapture('nivea.mp4')

lower_blue = np.array([95,50,50])
upper_blue = np.array([130,255,255])

kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
kernel_rectangular = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

while True:
    ret,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    result = cv2.bitwise_and(frame,frame,mask=mask)

    # Median
    median = cv2.medianBlur(mask,5)

    # Kernel 5x5
    kernel_5 = np.ones([5,5],dtype=np.uint8)

    # Erosion
    erosion = cv2.erode(mask,kernel=kernel_5,iterations=1)

    # Dilation
    dilation = cv2.dilate(mask,kernel=kernel_5,iterations=1)

    # Opening
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel_5)

    # Closing
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel_5)

    # Morphological Gradient
    gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel_5)

    cv2.imshow('result',result)
    cv2.imshow('mask',mask)
    cv2.imshow('median',median)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    cv2.imshow('gradient',gradient)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
