import extcolors

"""
@author = 'Ahmet Mucahit Tarakci'
"""

# Örnek resmimizin yolu
img_path = './sigortalar/orijinal/orijinal.jpg'

def ext_colors(img_path):
    # Renkler ve piksel sayılarının ataması
    colors, pixel_count = extcolors.extract(img_path)

    # Renklerin RGB değerleri ve piksel sayıları
    for i in range(len(colors)):
        print(colors[i])
    print('pixel_count:',pixel_count)
    print()
    print('-----returns as RGB-----')

    # Renklerin metin çıktısı
    i = 0
    while i < len(colors):
        print(str(colors[i][0]) + ': %' + str(round(((colors[i][1])/pixel_count)*100.0,2)))
        i += 1

    # Renklerin görsel çıktısı
    extcolors.image_result(colors,100,img_path)
    return colors

# RGB formatında döndürür
ext_colors(img_path=img_path)
