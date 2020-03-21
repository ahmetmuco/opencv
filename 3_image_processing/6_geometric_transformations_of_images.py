# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

"""
@author = 'Ahmet Mucahit Tarakci'
"""

# # Scaling (Ölçeklendirme)
# img = cv2.imread('001000071.jpg',0)
# cv2.imshow('image',img)
#
# resized_img = cv2.resize(img,None,fx=2, fy=2,
#                          interpolation=cv2.INTER_CUBIC)
# cv2.imshow('resized_img',resized_img)


# # Translation (Öteleme)
# img = cv2.imread('001000071.jpg',0)
# cv2.imshow('image',img)
# rows,cols = img.shape
#
# M = np.float32([[1,0,100],[0,1,50]])
# translated_img = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('translated_img',translated_img)
#
#
# # Rotation
# img = cv2.imread('001000071.jpg',0)
# cv2.imshow('image',img)
# rows,cols = img.shape
#
# M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# rotated_img = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('rotated_img',rotated_img)
#
#
# # Affine Transformation (Afin Dönüşüm)
# img = cv2.imread('cizim.png',1)
# cv2.imshow('image',img)
# rows, cols, ch = img.shape
#
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
#
# M = cv2.getAffineTransform(pts1,pts2)
#
# affine_transformed_img = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('affine_transformed_img',affine_transformed_img)
#
#
# Perspective Transformation
img = cv2.imread('Perspektif.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[0,0],[100,0],[0,160],[100,160]])
pts2 = np.float32([[0,0],[250,0],[0,250],[250,250]])

M = cv2.getPerspectiveTransform(pts1,pts2)

perspective_transformated_img = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Orijinal Goruntu')
plt.subplot(122),plt.imshow(perspective_transformated_img),plt.title('Sonuc')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
