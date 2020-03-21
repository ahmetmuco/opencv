from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab,deltaE_cie76
import os

"""
@author = 'Ahmet Mucahit Tarakci'
"""

IMAGE_DIRECTORY_PATH = './resimler'
COLORS = {
    'GREEN': [0,128,0],
    'BLUE': [0,0,128],
    'YELLOW': [255,255,0]
}
images = []


def get_image(image_path):
    image = cv2.imread(image_path)
    modified_image = cv2.resize(image,(600,400),interpolation=cv2.INTER_AREA)
    modified_image = cv2.cvtColor(modified_image,cv2.COLOR_BGR2RGB)
    return modified_image


for file in os.listdir(IMAGE_DIRECTORY_PATH):
    if not file.startswith('.'):
        images.append(get_image(os.path.join(IMAGE_DIRECTORY_PATH,file)))


# Show all images
plt.figure(figsize=(20,10))
for i in range(len(images)):
    plt.subplot(1,len(images),i + 1)
    plt.imshow(images[i])
plt.show()


def get_colors(image,number_of_colors,show_chart):
    # RGB to Hex Conversion
    def RGB2HEX(color):
        # ("#{:02x}{:02x}{:02x}".format(int(color[0]),int(color[1]),int(color[2])))
        return "#{:02x}{:02x}{:02x}".format(int(color[0]),int(color[1]),int(color[2]))

    # # resize 600x400
    # modified_image = cv2.resize(image,(600,400),interpolation=cv2.INTER_AREA)
    modified_image = image.reshape(image.shape[0] * image.shape[1],3)

    # KMeans clustering
    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)

    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if show_chart:
        plt.figure(figsize=(8,6))
        plt.pie(counts.values(),labels=hex_colors,colors=hex_colors)
        plt.show()

    return rgb_colors


def match_image_by_color(image,color,threshold=60,number_of_colors=10):
    image_colors = get_colors(image,number_of_colors,False)
    selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

    select_image = False
    for i in range(number_of_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = deltaE_cie76(selected_color,curr_color)
        if diff < threshold:
            select_image = True

    return select_image


def show_selected_images(images,color,threshold,colors_to_match):
    index = 1

    for i in range(len(images)):
        selected = match_image_by_color(images[i],
                                        color,
                                        threshold,
                                        colors_to_match)
        if selected:
            plt.subplot(1,len(images),index)
            plt.imshow(images[i])
            print(str(index) + ' image selected.')
            index += 1
    plt.show()


# Variable 'selected_color' can be any of COLORS['GREEN'], COLORS['BLUE'] or COLORS['YELLOW']
plt.figure(figsize=(20,10))
show_selected_images(images,COLORS['GREEN'],60,5)
