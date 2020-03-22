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
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
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

    def RGB2HEX(color):
        return "#{:02x}{:02x}{:02x}".format(int(color[0]),int(color[1]),int(color[2]))

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
    label_items = list(label_counts.items())
    print('label_items:',label_items)
    # print('label_counts.items():',label_counts.items())
    all_colors = clt.cluster_centers_

    # renklerin HEX karşılıklarının bulunması
    hex_colors = [RGB2HEX(all_colors[i]) for i in label_counts.keys()]
    print('HEX:',hex_colors)

    # renk kodlarının int tipine dönüşümü
    all_colors = all_colors.astype(int)

    # for i in range(len(all_colors)):
    #     for y in range(3):
    #         all_colors[i][y] = all_colors[i][y].astype(int)

    # atanan labellar ile RGB kodlarının eşlenmesi
    label_dict = {}
    for i in range(len(label_counts)):
        label_dict[str(label_items[i][0])] = all_colors[i]

    # eşlenen sözlüğü yazdır
    for k,v in label_dict.items():
        print(k,v)

    # print('Colors (RGB):')
    # for i in range(len(all_colors)):
    #     print(all_colors[i])

    print('**********************************************************')

    # return list(all_colors)

# toplam piksel sayısı bulunup hangi rengin yüzde kaç olduğu hesaplanabilir.
original_img = cv2.imread('./sigortalar/orijinal/orijinal.jpg',1)
original_img = cv2.cvtColor(original_img,cv2.COLOR_BGR2RGB)
get_dominant_color(image=original_img,k=4,image_processing_size=None)

for i in range(len(images)):
    get_dominant_color(image=images[i],k=4,image_processing_size=None)
