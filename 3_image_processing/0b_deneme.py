# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Kernel 3x3
kernel_3 = np.ones([3,3],dtype=np.uint8)
# Kernel 5x5
kernel_5 = np.ones([5,5],dtype=np.uint8)
# Kernel 7x7
kernel_7 = np.ones([7,7],dtype=np.uint8)
# Kernel 9x9
kernel_9 = np.ones([9,9],dtype=np.uint8)

kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
kernel_rectangular = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

img = cv2.imread('001000072.jpg',1)

# Convert BGR to HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  # HSV renk uzayına dönüştürüldü.

# define range of red color in HSV
# 0-10 Red
lower_red0 = np.array([0,0,70])
upper_red0 = np.array([180,130,255])
# 170-180 Red
lower_red1 = np.array([170,50,50])
upper_red1 = np.array([180,255,255])

# Threshold the HSV image to get only red colors
mask = cv2.inRange(hsv,lower_red0,upper_red0)  # Aralık değerlerini maskeye veriyoruz.

# # Smoothing
# kernel = np.ones((5,5),dtype=np.float32) / 25  # sondaki 25, kernelin boyutları carpımı. (5,5) ise sonu 25 gibi.
# smoothed = cv2.filter2D(result,-1,kernel)

# # Gaussian Blur
# gaussian_blur = cv2.GaussianBlur(result,(5,5),0)  # ilk parametre uygulanacak görüntü, ikinci parametre kernelsize

# Median
median = cv2.medianBlur(mask,7)
closing_red = cv2.morphologyEx(median,cv2.MORPH_CLOSE,kernel_5)
opening_red = cv2.morphologyEx(closing_red,cv2.MORPH_OPEN,kernel_5)
dilation_red = cv2.dilate(opening_red,kernel=kernel_7,iterations=1)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(img,img,mask=dilation_red)

# Bilateral Filtering
bilateral = cv2.bilateralFilter(mask,5,75,75)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('result',result)
cv2.imshow('hsv',hsv)
# cv2.imshow('smoothed',smoothed)
# cv2.imshow('gaussian_blur',gaussian_blur)
cv2.imshow('median',median)
cv2.imshow('closing_red',closing_red)
cv2.imshow('opening_red',opening_red)
cv2.imshow('dilation_red',dilation_red)
# cv2.imshow('bilateral',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
