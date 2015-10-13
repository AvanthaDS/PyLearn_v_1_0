__author__ = 'Avantha'

from PIL import Image

img = Image.open('s2.jpg')
me_img= Image.open('s.jpg')

#print(img.size)
#print(img.format)
print(img.mode)




'''area = (200,200,330,340)
cropped_img = img.crop(area)'''

r, g, b = img.split()
r2,g2,b2 = me_img.split()

newImg = Image.merge('RGB',(g,g,b))

#area = (100,100,239,240)

#img.paste(me_img,area)

print(me_img.size)
print(me_img.mode)
'''r.show()
g.show()
b.show()
a.show()'''
newImg.show()

#img.show()
#cropped_img.show()


