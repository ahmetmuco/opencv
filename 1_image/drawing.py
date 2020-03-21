# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Create a black image (siyah arkaplanı olan resim yapıldı(512x512 boyutunda))
img = np.zeros((512, 512, 3))

# Drawing Line
    # Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)   # (0,0) başlama koordinatı; (511,511) bitiş koordinatı; renk ve kalınlık.

# Drawing Rectangle (Kare)
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)   # kare için (384,0) sol üst köşesi; (512,128) sağ alt köşesi belirtildi.

# Drawing Circle
img = cv2.circle(img, (447,63), 63, (0,0,255), -1)

# Drawing Ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Drawing Polygon(çokgen)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)   # 4 kenarlı şeklin koordinatları listeye atandı.
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# Adding Text to Images
font = cv2.FONT_HERSHEY_SIMPLEX   # font belirle
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

# resmi göster
cv2.imshow('img', img)
cv2.waitKey(0)