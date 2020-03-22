from sklearn.cluster import KMeans
from collections import Counter
import cv2  # for resizing image
import matplotlib.pyplot as plt
import numpy as np
import os

IMAGE_DIRECTORY_PATH = './sigortalar/denemeler'
images = []


def get_image(image_path):
    image = cv2.imread(image_path,1)
    return image


for file in os.listdir(IMAGE_DIRECTORY_PATH):
    if not file.startswith('.'):
        images.append(get_image(os.path.join(IMAGE_DIRECTORY_PATH,file)))


def get_dominant_color(image,k=4,image_processing_size=None):
    # resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image,image_processing_size,
                           interpolation=cv2.INTER_AREA)
        # cv2.imshow('img func',image)

    # reshape the image to be a list of pixels
    image_reshaped = image.reshape((image.shape[0] * image.shape[1],3))

    # cluster and assign labels to the pixels
    clt = KMeans(n_clusters=k)
    labels = clt.fit_predict(image_reshaped)
    print('labels:',np.unique(labels))

    # count labels to find most popular
    label_counts = Counter(labels)

    # subset out most popular centroid
    # dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    print('label_counts.items():',label_counts.items())
    all_colors = clt.cluster_centers_

    print('Colors (BGR):')
    for i in range(len(all_colors)):
        print(all_colors[i])
    print('**********************************************************')

    # return list(all_colors)

original_img = cv2.imread('./sigortalar/orijinal/orijinal.jpg',1)
get_dominant_color(image=original_img,k=4,image_processing_size=None)

for i in range(len(images)):
    get_dominant_color(image=images[i],k=4,image_processing_size=None)
