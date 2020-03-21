# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Green
lower_green = np.array([40,52,72])
upper_green = np.array([80,255,255])

# Red
lower_red = np.array([0, 100, 80])
upper_red = np.array([10, 255, 255])

# Kernel 3x3
kernel_3 = np.ones([3,3],dtype=np.uint8)
# Kernel 5x5
kernel_5 = np.ones([5,5],dtype=np.uint8)
# Kernel 7x7
kernel_7 = np.ones([7,7],dtype=np.uint8)
# Kernel 9x9
kernel_9 = np.ones([9,9],dtype=np.uint8)

# Original Image
img = cv2.imread('resim.PNG',1)

# HSV Color space
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Mask green
mask_green = cv2.inRange(hsv,lower_green,upper_green)

# Mask red
mask_red = cv2.inRange(hsv,lower_red,upper_red)

# Morphology green
median_green = cv2.medianBlur(mask_green,3)

# Morphology red
median_red = cv2.medianBlur(mask_red,3)

# Result green
result_green = cv2.bitwise_and(img,img,mask=median_green)

# Result red
result_red = cv2.bitwise_and(img,img,mask=median_red)

# Final image
mask_final = cv2.add(median_red,median_green)
result = cv2.bitwise_and(img,img,mask=mask_final)

cv2.imshow('img',img)
cv2.imshow('mask_green',mask_green)
cv2.imshow('median_green',median_green)
cv2.imshow('result_green',result_green)
cv2.imshow('mask_red',mask_red)
cv2.imshow('median_red',median_red)
cv2.imshow('result_red',result_red)
cv2.imshow('result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()
