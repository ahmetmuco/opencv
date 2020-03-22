# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import numpy as np

"""

@author = 'Ahmet Mucahit Tarakci'
"""

IMAGE_DIRECTORY_PATH = './sigortalar/orijinal/orijinal.jpg'

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i","--image",required=True,help="Path to the image")
# ap.add_argument("-c","--clusters",required=True,type=int,
#                 help="# of clusters")
# args = vars(ap.parse_args())

# load the image and convert it from BGR to RGB so that
# we can display it with matplotlib
image = cv2.imread(IMAGE_DIRECTORY_PATH)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# show our image
plt.figure(figsize=(10,5))
plt.axis("off")
plt.subplot(1,2,1)
plt.imshow(image)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))

# cluster the pixel intensities
kmeans = KMeans(n_clusters=4)
labels = kmeans.fit_predict(image)
print('cluster_centers_:',kmeans.cluster_centers_)
print('kmeans.labels_:',kmeans.labels_)
print('np.unique(labels):',np.unique(labels))

def centroid_histogram(kmeans):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(kmeans.labels_)) + 1)
	(hist, _) = np.histogram(kmeans.labels_, bins = numLabels)
	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()
	# return the histogram
	return hist

def plot_colors(hist,centroids):
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50,300,3),dtype="uint8")
	startX = 0
	# loop over the percentage of each cluster and the color of
	# each cluster
	for (percent,color) in zip(hist,centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv2.rectangle(bar,(int(startX),0),(int(endX),50),color.astype("uint8").tolist(),-1)
		startX = endX

	# return the bar chart
	return bar

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = centroid_histogram(kmeans)
bar = plot_colors(hist, kmeans.cluster_centers_)
# show our color bart
# plt.figure()
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(bar)
plt.show()