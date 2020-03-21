# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('messi.jpg')
# plt.imshow(img)
# plt.show()

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

px = img[100,100]  # BGR değerlerini döndürür.
print('100x100 noktası:', px)

pxBlue = img[100,100,0]  # sadece blue değerini atadık.
print('100x100 noktasının blue değeri:', pxBlue)

img[100,100] = [255,255,255]  # x=100, y=100 pikselini beyaz yaptık. (sağ kolunda)
print('100x100 noktasına beyaz atandı:', img[100,100])

bolge = img[50:100,100:150]
img[50:100,100:150] = [255,255,255]
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Better pixel accessing and editing method:
# img.item() ile piksele ulaşıp, img.itemset() ile pikselin değerini değiştiriyoruz.
print('red: ', img.item(10,10,2))  # kırmızıya ulaştık.
img.itemset((10,10,2),255)
print('itemset:', img.item(10,10,2))

print('image shape:', img.shape) # resim boyutu
print('image size:', img.size) # bütün piksellerin sayısı
print('image dtype:', img.dtype) # resmin veritipi

# Image ROI (region of images)
top = img[265:320, 310:365] # topun oldugu pikselleri tespit edip top dizisine atadık.
img[200:255, 100:155] = top # piksel sayılarına dikkat ederek(top dizisinin boyutu ile img üzerinde seçilen yerin aynı boyutta olması lazım) top kopyalandı.
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Splitting and Merging Image Channels
# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r)) # cv2 kütüphanesinde yapımı
b = img[:,:,0] # blue değerine ulaştık.
img[:,:,2] = 0 # bütün resim üzerindeki kırmızıları 0 yaptık. resmin rengi değişti.
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Making Borders for Images (Padding) (Burada olmadı sitede düzgün) (1a)
# BLUE = [255,0,0]
# img1 = cv2.imread('OpenCV-logo.png')
#
# replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
# constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
#
# plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
#
# plt.show()