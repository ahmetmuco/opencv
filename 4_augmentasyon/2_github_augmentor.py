# -*- coding: utf-8 -*-
import Augmentor

"""
@author = 'Ahmet Mucahit Tarakci'
"""

path_to_android = "./android"
path_android_mask = "./android_mask"

# Ground Truth Data
# Hat oluşturma:
p = Augmentor.Pipeline(path_to_android)

# Orijinal veriler
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.sample(2)

# Groud Truth Hattı
p.ground_truth(path_android_mask)

p.rotate(probability=1, max_left_rotation=5, max_right_rotation=5)
p.flip_left_right(probability=0.5)
p.zoom_random(probability=0.5, percentage_area=0.8)
p.flip_top_bottom(probability=0.5)
p.sample(2)
