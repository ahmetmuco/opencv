# -*- coding: utf-8 -*-
import numpy as np
import cv2

feyyaz_yigit = cv2.imread('feyyaz_yigit.jpg')
android = cv2.imread('android.jpg')

android_gray = cv2.cvtColor(android,cv2.COLOR_BGR2GRAY) # Üzerinde çalışmak daha kolay olacağından gri kanala dönüştürüldü-
# ve maskeleme için zemin hazırlandı.

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = android.shape # eklenecek olan logonun boyutlarında roi oluşturuldu.
roi = feyyaz_yigit[0:rows,0:cols]

# Now create a mask of logo and create its inverse mask also
ret, mask = cv2.threshold(android_gray,10,255,cv2.THRESH_BINARY) # mask değişkenine 10 threshhold'u verildi yani gri kanal üzerinde-
# değeri 10'dan büyük olan pikseller bir sonraki parametrede verilen 255 değeri ile değiştirildi.
mask_inv = cv2.bitwise_not(mask) # piksellerin tersi de alındı.

# Now black-out the area of logo in ROI
feyyaz_yigit_roi = cv2.bitwise_and(roi,roi,mask=mask_inv) # belirlediğimiz roi üzerinde siyah androidi verdik-
# bitwise_and işlemi, pikselleri 've' işlemine tabii tutuyor. 1v0=0, 1v1=1. bitler üzerinde 've' işlemi uygulayarak-
# ters maskeledigimiz logo ile logoyu koymak istediğimiz yere 've' işlemi uyguluyoruz ve arkaplan renklerini kaybetmiyoruz.
# siyah baskın renk, beyaz çekingen renk. Arkaplanın rengi ile beyaz rengi 've' işlemine tabii tutarsak arkaplan rengi galip-
# gelir ve arkaplan rengi korunur. Koymak istediğimiz android logosu siyah renkte oldugundan baskın olacak ve galip gelecektir.

# Take only region of logo from logo image. (Bunu anlamadım??????????????)
android_fg = cv2.bitwise_and(android,android,mask=mask)

# Put logo in ROI and modify the main image
toplam = cv2.add(feyyaz_yigit_roi,android) # roi ile yeşil renkteki android resmini cv2.add() ile birleştiriyoruz ve-
# renk bitleri toplanıyor. Android arkaplanı siyah iken yani bir değerleri 0 iken, feyyaz yiğit'in resminin arkaplanındaki-
# renk bitleri ile toplanıyor ve arkaplan renkli oluyor.
feyyaz_yigit[0:rows,0:cols] = toplam # asıl feyyaz yiğit resmi üzerine ekliyoruz.



# cv2.imshow('FEYYAZ_YIGIT',feyyaz_yigit)
# cv2.imshow('ANDROID',android)
# cv2.imshow('ANDROID_GRAY',android_gray)
# cv2.imshow('ROI',roi)
cv2.imshow('MASKED_ANDROID',mask)
cv2.imshow('MASK_INV',mask_inv)
cv2.imshow('feyyaz_yigit_roi',feyyaz_yigit_roi)
cv2.imshow('toplam',toplam)
cv2.imshow('android_fg',android_fg)
cv2.imshow('FEYYAZ_YIGIT_SON',feyyaz_yigit)
cv2.imwrite('feyyaz_yigit_android.png',feyyaz_yigit)



cv2.waitKey(0)
cv2.destroyAllWindows()