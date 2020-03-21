# -*- coding: utf-8 -*-
import imageio
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np

"""
@author = 'Ahmet Mucahit Tarakci'
"""

path = './resimler/saü-logo.PNG'
img = imageio.imread(path)

# # Orijinal resim:
# ia.imshow(img)
#
# # -45 veya 45 derece döndürme:
# rotate = iaa.Affine(rotate=(-45, 45))
# image_aug = rotate(image=img)
#
# # Augmented:
# ia.imshow(image_aug)


# # Birden fazla resim üzerinde işlem yapmak:
images = [img, img, img, img]
#
# # -45 veya 45 derece döndürme:
# rotate = iaa.Affine(rotate=(-45, 45))
# images_aug = rotate(images=images)
#
# # Zenginleştirilmiş Görüntüler:
# ia.imshow(np.hstack(images_aug))


# Eşzamanlı Olarak Birden Fazla Zenginleştirme Tekniği:
seq = iaa.Sequential([
    iaa.Affine(rotate=(-45, 45)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2))
])
# Zenginleştirme çağrısı:
images_aug = seq(images=images)

# Zenginleştirilmiş esimler:
ia.imshow(np.hstack(images_aug))