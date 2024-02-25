import math

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def pixel2ascii(pixel):
    density = 'Ñ@#W$9876543210?!abc;:+=-,._ '
    L = len(density)

    frac = pixel/255
    index = math.floor(frac*L)
    #print(index)
    return density[index]

image = mpimg.imread('image.jpeg')

gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

plt.imshow(gray_image, cmap='gray')
#plt.show()

ascii_image = np.vectorize(pixel2ascii)(gray_image)
#print(ascii_image)

np.savetxt('ascii.txt', ascii_image, fmt='%s')

