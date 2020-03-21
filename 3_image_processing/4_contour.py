# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os
"""
@author = 'Ahmet Mucahit Tarakci'
"""
# Blue
lower_blue = np.array([90,50,80])
upper_blue = np.array([130,255,255])

# Red
lower_red = np.array([0,0,55])
upper_red = np.array([180,135,255])

# Kernel 3x3
kernel_3 = np.ones([3,3],dtype=np.uint8)
# Kernel 5x5
kernel_5 = np.ones([5,5],dtype=np.uint8)
# Kernel 7x7
kernel_7 = np.ones([7,7],dtype=np.uint8)
# Kernel 9x9
kernel_9 = np.ones([9,9],dtype=np.uint8)

for file in os.listdir('.'):
    if file.endswith('.jpg'):
        # Original image
        img = cv2.imread(file,1)

        # Convert to HSV color space
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        # Masks
        mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
        mask_red = cv2.inRange(hsv,lower_red,upper_red)

        # Morphological Transformations
        # Blue mask
        opening_blue = cv2.morphologyEx(mask_blue,cv2.MORPH_OPEN,kernel_5)
        dilation_blue = cv2.dilate(opening_blue,kernel=kernel_5,iterations=1)
        # Red mask
        median_red = cv2.medianBlur(mask_red,9)
        closing_red = cv2.morphologyEx(median_red,cv2.MORPH_CLOSE,kernel_5)
        opening_red = cv2.morphologyEx(closing_red,cv2.MORPH_OPEN,kernel_5)
        dilation_red = cv2.dilate(opening_red,kernel=kernel_7,iterations=1)

        # Contour blue
        ret,thresh = cv2.threshold(dilation_blue,127,255,0)
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(img,contours,-1,(0,255,0),3)

        # Center of blue objects
        for c in contours:
            M = cv2.moments(c)

            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.circle(img,(cX,cY),5,(255,0,0),-1)
            cv2.putText(img,"",(cX - 25,cY - 25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

        # Contour red
        ret,thresh = cv2.threshold(dilation_red,127,255,0)
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(img,contours,-1,(0,255,0),3)

        # Center of red objects
        for c in contours:
            M = cv2.moments(c)

            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.circle(img,(cX,cY),5,(255,0,0),-1)
            cv2.putText(img,"",(cX - 25,cY - 25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

        # Only blue
        result_blue = cv2.bitwise_and(img,img,mask=dilation_blue)
        # Only red
        result_red = cv2.bitwise_and(img,img,mask=dilation_red)

        # Final image
        result = cv2.add(result_blue,result_red)

        cv2.imshow('result',result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
