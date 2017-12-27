from PIL import Image

size = 1000, 1000

# image_size = Image.open('1.png').thumbnail(size, Image.ANTIALIAS)
# image = Image.open('1.png')

basewidth = 2000
img = Image.open('1.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('1.png')
img.show()
