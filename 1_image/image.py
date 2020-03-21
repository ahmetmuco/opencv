# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:36:40 2020

@author: Ahmet
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load an color image in grayscale
image = cv2.imread('messi.jpg',0)  # -1, 0 ve 1 flag parametreleri var. 0 gri; 1 renkli; -1 alpha channel(?)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()  # pencerenin kapanması için

# farklı bir resim
globalCat = cv2.imread('globalCat.jpg',1)
cv2.namedWindow('globalCat',cv2.WINDOW_NORMAL)  # default olarak WINDOW_AUTOSIZE fakat WINDOW_NORMAL da boyutlandırma faln 99_bişeyler
cv2.imshow('globalCat',globalCat)
cv2.waitKey(0)
cv2.destroyAllWindows()  # pencerenin kapanması için

# matplot ile gösterme
plt.imshow(image,cmap='gray',interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
