from PIL import Image
import sys
#python lab2\\task2.py lab2\\Photos\\Cat.jpg

img = Image.open(sys.argv[1])
data = img.getdata()
r = [(d[0], 0, 0) for d in data if d[0] != 0]
g = [(0, d[1], 0) for d in data if d[1] != 0]
b = [(0, 0, d[2]) for d in data if d[2] != 0]

print('RED:\t', len(r))
print('GREEN:\t', len(g))
print('BLUE:\t', len(b))
