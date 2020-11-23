# -*- coding: utf-8 -*-
import imageio
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np

"""
@author = 'Ahmet Mucahit Tarakci'
"""

path = 'C:\\Users\\Ahmet\\Desktop\\opencv\\4_augmentasyon\\buyuk_sigorta\\001000014.jpg'

resim = imageio.imread(path)
resimler = [resim, resim, resim, resim]

# Eşzamanlı Olarak Birden Fazla Çoğaltma Tekniği:
seq = iaa.Sequential([
    iaa.Affine(rotate=(-45, 45)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2))
])

# Veri çoğaltma çağrısı:
augmentasyon_islemi = seq(images=resimler)

# Çoğaltılmış resimler:
ia.imshow(np.hstack(augmentasyon_islemi))
