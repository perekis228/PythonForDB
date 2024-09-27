from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("../lab2/Photos/Cat.jpg")

hist = img.histogram()
red = hist[0:256]
green = hist[256:512]
blue = hist[512:768]

plt.imshow(img)
fig, axs = plt.subplots(nrows=4)
for num, color_name, color in (0, 'black', hist), (1, 'red', red), (2, 'green', green), (3, 'blue', blue):
    axs[num].plot(color, c=color_name)
    axs[num].set_title(color_name)
plt.show()