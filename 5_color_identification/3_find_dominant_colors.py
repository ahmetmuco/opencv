from sklearn.cluster import KMeans
from collections import Counter
import cv2  # for resizing image
import matplotlib.pyplot as plt
import numpy as np


def get_dominant_color(image,k=4,image_processing_size=None):
    """
    takes an image as input
    returns the dominant color of the image as a list

    dominant color is found by running k means on the
    pixels & returning the centroid of the largest cluster

    processing time is sped up by working with a smaller image;
    this resizing can be done with the image_processing_size param
    which takes a tuple of image dims as input

    # >>> get_dominant_color(my_image, k=4, image_processing_size = (25, 25))
    [56.2423442, 34.0834233, 70.1234123]
    """
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

    return list(all_colors)

original_img = cv2.imread('./sigortalar/orijinal/orijinal.jpg',1)
colors = get_dominant_color(image=original_img,k=4,image_processing_size=None)
# returns as BGR
# print('One Dominant Color as BGR Mode:',end='')
# print('Colors (BGR):')
# for i in range(len(colors)):
#     print(colors[i])

# image_gray = cv2.cvtColor(original_img,cv2.COLOR_RGB2GRAY)
# ret,thresh = cv2.threshold(image_gray,50,255,cv2.THRESH_BINARY)
# contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # images[i] = cv2.drawContours(images[i],contours,-1,(0,255,0),2)
# for c in contours:
#     # compute the bounding box of the contour andq then draw the
#     # bounding box on both input images to represent where the two
#     # images differ
#     (x,y,w,h) = cv2.boundingRect(c)
#     cv2.rectangle(original_img,(x,y),(x + w,y + h),(0,255,0),2)
# cv2.imshow('image',original_img)
# cv2.waitKey()
# cv2.destroyAllWindows()