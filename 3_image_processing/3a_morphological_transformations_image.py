import numpy as np
import cv2

# Green
lower_green = np.array([40,52,72])
upper_green = np.array([80,255,255])

# Kernel Oluşturma
kernel_5 = np.ones([5,5],dtype=np.uint8)

# Original image
img = cv2.imread('resim.PNG',1)

# HSV color space
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Mask green
mask = cv2.inRange(hsv,lower_green,upper_green)

# Median
median = cv2.medianBlur(mask,5)

# Normal mask result
result = cv2.bitwise_and(img,img,mask=mask)

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

cv2.imshow('img',img)
cv2.imshow('result',result)
cv2.imshow('mask',mask)
cv2.imshow('median',median)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)
cv2.imshow('gradient',gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
