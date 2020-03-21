# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Image Addition
# cv2.add() fonksiyonu ve direkt olarak numpy eklemesi de var.
# cv2.add() doygunluga göre ekler; numpy modüler bölme yapıp ekler.
x = np.uint8([250])
y = np.uint8([10])
print('cv2.add() fonk ile:',cv2.add(x,y))  # 250+10 = 260 => 255
print('numpy:',x + y)  # 250+10 = 260 % 256 = 4
# It will be more visible when you add two images. OpenCV function will provide a better result. So always better stick to OpenCV functions.
# cv2.add() kullan.

# Image Blending (Resim harmanlama/karıştırma)
# resimlere ağırlık vererek resimleri harmanlar.
img1 = cv2.imread('tree_fog_grass_119819_800x600.jpg')
img2 = cv2.imread('girl_field_wind_122296_800x600.jpg')
# boyutları aynı olmalı(?)
new_img = cv2.addWeighted(img1,0.4,img2,0.6,0)
cv2.imshow('new_img',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('agirlikli_harmanlama.png',new_img)