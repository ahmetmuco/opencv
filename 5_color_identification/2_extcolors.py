import extcolors
import time

"""
@author = 'Ahmet Mucahit Tarakci'
"""

start_time = time.time()

img_path = './sigortalar/000_SET028_CAM1_OK__83_.jpg'

colors, pixel_count = extcolors.extract(img_path)
print(colors)
print(pixel_count)

i = 0
while i < len(colors):
    print(str(colors[i][0]) + ': %' + str(round(((colors[i][1])/pixel_count)*100.0,2)))
    i += 1

# extcolors.image_result(colors,100,img_path)

end_time = time.time()
print('Done in ' + str(round(end_time - start_time,2)) + ' seconds.')
