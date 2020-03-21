# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Original image
img_rgb = cv2.imread('001000070b.jpg')
# BGR2GRAY
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Object that we are gonna search
template = cv2.imread('fuse.png',0)
# Template image shape
w, h = template.shape[::-1]
# matchTemplate function
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# Threshold of similarity
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)

# cv2.imwrite('fuses.png',img_rgb)
cv2.imshow('img_rgb',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
