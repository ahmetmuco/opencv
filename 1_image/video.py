# -*- coding: utf-8 -*-
import numpy as np
import cv2

# 0 -> Bilgisayar kamerası
# 1 -> USB takılı kamera
# Video Adresi ve adı -> Diskteki bir video

kamera = cv2.VideoCapture('video.mp4')

# kamera.set(3,520) # 3 -> Genişlik
# kamera.set(4,360) # 4 -> Yükseklik
# Videoda çalışmadı.

def ayarlama(frame,yuzde=75):
    genislik = int(frame.shape[1] * yuzde / 100)
    yukseklik = int(frame.shape[0] * yuzde / 100)
    boyut = (genislik,yukseklik)
    return cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA)


while True:
    ret,frame = kamera.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    frame2 = ayarlama(frame,50)

    cv2.imshow('Orijinal Video',frame)
    cv2.imshow('Boyutlandirilmis Video',frame2)
    cv2.imshow('Gray Video',frame_gray)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
