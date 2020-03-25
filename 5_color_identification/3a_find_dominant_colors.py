from sklearn.cluster import KMeans
from collections import Counter
import cv2
import numpy as np
import os

IMAGE_DIRECTORY_PATH = './resimler/resim_300'
images = []

# Resimlere ulaşılması ve RGB renk formatına dönüşümü
def get_image(image_path):
    image = cv2.imread(image_path,1)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image


for file in os.listdir(IMAGE_DIRECTORY_PATH):
    if not file.startswith('.'):
        images.append(get_image(os.path.join(IMAGE_DIRECTORY_PATH,file)))


def get_colors(image,k=4,image_processing_size=None):
    # Size (Boyut) belirtildi ise resmi boyutlandırma işlemi
    if image_processing_size is not None:
        image = cv2.resize(image,image_processing_size,
                           interpolation=cv2.INTER_AREA)

    # Resmin çok boyutlu piksel matrisine dönüşümü
    image_reshaped = image.reshape((image.shape[0] * image.shape[1],3))

    # Kümeleme ve etiketleme işlemi
    clt = KMeans(n_clusters=k)
    labels = clt.fit_predict(image_reshaped)
    print('labels:',np.unique(labels))

    # Counter ile etiketlerin sıralanması
    label_counts = Counter(labels)

    # Etiketlerin ve piksel sayılarının listeye atanması
    label_items = list(label_counts.items())
    print('Etiketler:',label_items)

    # Renk kodlarının atanması
    all_colors = clt.cluster_centers_

    # Renk kodlarının int tipine dönüşümü
    all_colors = all_colors.astype(int)

    # Atanan labellar ile RGB kodlarının eşlenmesi
    label_dict = {}
    for i in range(len(label_counts)):
        label_dict[str(label_items[i][0])] = all_colors[i]

    # Eşlenen sözlüğü yazdır
    for k,v in label_dict.items():
        print('Etiket Kodu: {0} -> RGB Degerleri: {1}'.format(k,v))

    print('**********************************************************')

# Fonksiyon çağrısı
for i in range(len(images)):
    get_colors(image=images[i],k=4,image_processing_size=None)

