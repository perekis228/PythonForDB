from PIL import Image

img = Image.open('Photos/CatRGB.jpg')
img.show()
data = img.getdata()
r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]

img.putdata(r)
img.show()
img.putdata(g)
img.show()
img.putdata(b)
img.show()