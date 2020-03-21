# -*- coding: utf-8 -*-
from PIL import Image

# image = Image.open('messi.jpg')
# image.rotate(45).show()

size = (200,200)

# for infile in glob.glob("*.jpg"):
#     file, ext = os.path.splitext(infile)
#     im = Image.open(infile)
#     im.thumbnail(size)
#     im.save(file + ".thumbnail", "JPEG")


img = Image.open('001000071.jpg',mode='r')
img.show()
print('img.getbands():',img.getbands())  # Bantları döndürür. RGB ise ('R','G','B') gibi.
print('img.getcolors():',img.getcolors(maxcolors=256))
print('img.mode:',img.mode)  # RGB döndürdü.
print('img.size:',img.size)  # Resmin boyutlarını tuple olarak döndürdü.
print('img.format:',img.format)  # Resmin formatını döndürdü. JPEG, PNG

# img.resize(size,resample=0).show()  # sonuna show() koyulabilir ve direkt olarak resized hali görüntülenebilir.
img2 = img.resize(size,resample=0)  # başka bir değişkene resized hali atanabilir.
# img2.show()
# img = Image.new('RGB',size=size,color=0)
img2.thumbnail(size)
img2.save('img2_resized.jpg',format=None)
# img.show(title='asd')
