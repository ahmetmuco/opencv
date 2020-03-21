# -*- coding: utf-8 -*-
import numpy as np
import cv2

# mask farklılıkları var.

# resimleri ekle
feyyaz_yigit_android = cv2.imread('feyyaz_yigit_android.png')
frog = cv2.imread('frog.jpg')

# roi
rows, cols, channels = frog.shape
roi = feyyaz_yigit_android[0:rows,1000:1000+cols]
# cv2.imshow('ROI',roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# gri yapma ve mask
frog_gray = cv2.cvtColor(frog,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(frog_gray,190,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# feyyaz yiğit arkaplan
feyyaz_yigit_android_roi = cv2.bitwise_and(roi,roi,mask=mask)

# frog önplan
frog_fg = cv2.bitwise_and(frog,frog,mask=mask_inv)

# birleştirme
toplam = cv2.add(feyyaz_yigit_android_roi,frog_fg)
feyyaz_yigit_android[0:rows,1000:1000+cols] = toplam

cv2.imshow('feyyaz', feyyaz_yigit_android)
cv2.imshow('frog', frog)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('frog_fg',frog_fg)
cv2.imshow('feyyaz_yigit_android_roi', feyyaz_yigit_android_roi)
cv2.imwrite('feyyaz_yigit_android_frog.png',feyyaz_yigit_android)
cv2.waitKey(0)