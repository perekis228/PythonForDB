from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("../lab2/Photos/Cat.jpg")

hist = img.histogram()
red = hist[0:256]
green = hist[256:512]
blue = hist[512:768]

fg = plt.figure(figsize=(9, 4), constrained_layout=True)
gs = fg.add_gridspec(4, 2)

fg.add_subplot(gs[:, 0])
plt.imshow(img)
plt.xticks([])
plt.yticks([])

for num, color_name, color in (0, 'black', hist), (1, 'red', red), (2, 'green', green), (3, 'blue', blue):
    fg.add_subplot(gs[num, 1])
    plt.plot(color, c=color_name)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
plt.show()
