# -*- coding: utf-8 -*-
import Augmentor

"""
@author = 'Ahmet Mucahit Tarakci'
"""

# Verilerimizin yolu:
path_to_data = "./resimler/"

# Hat oluşturma:
p = Augmentor.Pipeline(path_to_data)

# Random Erasing:
p.random_erasing(probability=1,
                 rectangle_area=1)


# # Flip:
# p.flip_random(probability=1)


# # Crop:
# p.crop_random(probability=1,
#               percentage_area=0.8,
#               randomise_percentage_area=True)


# # Skew:
# p.skew(probability=1,magnitude=1)

# p.skew_left_right(probability=1,magnitude=1)


# # Random Distortion:
# p.random_distortion(probability=1,
#                     grid_width=4,
#                     grid_height=4,
#                     magnitude=8)


# Number of samples:
num_of_samples = 10

# Örnekleri oluşturma:
p.sample(num_of_samples)
