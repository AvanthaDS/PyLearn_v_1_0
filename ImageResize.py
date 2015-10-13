__author__ = 'Avantha'

from PIL import Image
from PIL import ImageFilter

img = Image.open('s2.jpg')
img2 = Image.open('img1.png')

bw = img2.convert('L')
blurr = img.filter(ImageFilter.BLUR)
det = img.filter(ImageFilter.DETAIL)
edge = img.filter(ImageFilter.FIND_EDGES)



large = img.resize((500,500))
flip = img.transpose(Image.FLIP_LEFT_RIGHT)
large_flip =flip.resize((500,500))
rotate = large_flip.transpose(Image.ROTATE_270)

#img.show()
'''large.show()
large_flip.show()
rotate.show()'''
#bw.show()
blurr.show()
det.show()
edge.show()