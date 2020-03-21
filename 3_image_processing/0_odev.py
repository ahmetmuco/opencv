# -*- coding: utf-8 -*-
import numpy as np
import cv2
from PIL import Image

# Blue
lower_blue = np.array([90,50,50])
upper_blue = np.array([130,255,255])

# 0-10 Red
lower_red0 = np.array([0,50,50])
upper_red0 = np.array([10,255,255])
# 170-180 Red
lower_red1 = np.array([170,50,50])
upper_red1 = np.array([180,255,255])

kernel = np.ones([5,5],dtype=np.uint8)

img = cv2.imread('001000073.jpg',1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
mask_red_lower = cv2.inRange(hsv,lower_red0,upper_red0)
mask_red_upper = cv2.inRange(hsv,lower_red1,upper_red1)
mask_red = cv2.add(mask_red_lower,mask_red_upper)

# dilation = cv2.dilate(mask_red,kernel=kernel,iterations=1)

# erosion_red = cv2.erode(mask_red,kernel,iterations = 1)
opening_red = cv2.morphologyEx(mask_red,cv2.MORPH_OPEN,kernel)
closing_red = cv2.morphologyEx(opening_red,cv2.MORPH_CLOSE,kernel)
closing_blue = cv2.morphologyEx(mask_blue,cv2.MORPH_CLOSE,kernel)

median_red = cv2.medianBlur(closing_red,5)

result_blue = cv2.bitwise_and(img,img,mask=closing_blue)
result_red = cv2.bitwise_and(img,img,mask=median_red)

# Final Picture
result = cv2.add(result_red,result_blue)

cv2.imshow('img',img)
cv2.imshow('hsv',hsv)
cv2.imshow('mask_blue',mask_blue)
cv2.imshow('closing_blue',closing_blue)
cv2.imshow('mask_red',mask_red)
cv2.imshow('closing_red',closing_red)
cv2.imshow('opening_red',opening_red)
# cv2.imshow('erosion_red',erosion_red)
# cv2.imshow('dilation',dilation)
cv2.imshow('result_blue',result_blue)
cv2.imshow('result_red',result_red)
cv2.imshow('median_red',median_red)
cv2.imshow('result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()