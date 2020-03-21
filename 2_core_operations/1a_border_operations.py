# -*- coding: utf-8 -*-
import numpy as np
import cv2

# Orijinal Resim
img = cv2.imread('frog.jpg')
cv2.imshow('FROG', img)
cv2.waitKey(0)

# Resmi Uzatma
uzatilan_resim = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REPLICATE)
cv2.imshow('uzatilan_resim', uzatilan_resim)
cv2.waitKey(0)

# Resmi Aynalama
aynala_resim = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REFLECT)
cv2.imshow('aynala_resim', aynala_resim)
cv2.waitKey(0)

# Resim Tekrar Etme
tekrarlanan_resim = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_WRAP)
cv2.imshow('tekrarlanan_resim', tekrarlanan_resim)
cv2.waitKey(0)

# Resim Etrafını Sarma(Cerceve)
sarilan_resim = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_CONSTANT, value=[255,0,0])
cv2.imshow('sarilan_resim', sarilan_resim)
cv2.waitKey(0)
cv2.imwrite('frog_cerceve.png',sarilan_resim)

# Kare Çizme
img = cv2.rectangle(img, (90,40), (140,80), (0,255,0), 2)
cv2.imshow('FROG_KARE', img)
cv2.waitKey(0)

cv2.destroyAllWindows()