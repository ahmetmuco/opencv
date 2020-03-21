# -*- coding: utf-8 -*-
import numpy as np
import cv2
import Augmentor

"""
@author = 'Ahmet Mucahit Tarakci'
"""

"""
p = Augmentor.Pipeline("./resimler")
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.sample(100)
"""

path_to_data = "./resimler/"

# Create a pipeline
p = Augmentor.Pipeline(path_to_data)

# Add some operations to an existing pipeline.

# First, we add a horizontal flip operation to the pipeline:
p.flip_left_right(probability=0.4)

# Now we add a vertical flip operation to the pipeline:
p.flip_top_bottom(probability=0.8)

# Add a rotate90 operation to the pipeline:
p.rotate90(probability=0.1)

# Here we sample X images from the pipeline.

# It is often useful to use scientific notation for specify
# large numbers with trailing zeros.
# num_of_samples = int(1e5)
num_of_samples = 1000

# Now we can sample from the pipeline:
p.sample(num_of_samples)
