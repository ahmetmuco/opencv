# -*- coding: utf-8 -*-
import numpy as np
import cv2

def main():
    img = cv2.imread('android.jpg')
    print(img.shape)

    iki_kat_buyut = cv2.pyrUp(img)
    iki_kat_kucult = cv2.pyrDown(img)

    cv2.imshow('Android',img)
    cv2.imshow('Buyuk',iki_kat_buyut)
    cv2.imshow('Kucuk',iki_kat_kucult)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()