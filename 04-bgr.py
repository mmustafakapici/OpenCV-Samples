from cv2 import cv2

import numpy as np

image = cv2.imread("kus.jpg" ) # 0: grayscale, 1: color

cv2.imshow("image", image)

print(image[(230,80)])

#shape
print('shape:',image.shape)

#boyut
print('boyut:',image.size)

#veri tipi
print('veri tipi:',image.dtype)

#piksel rengi değiştirme
image[80,80] = [255,255,255]

for i in range(100):
   image[70, i ]= [255,255,255]


cv2.waitKey(0)
cv2.destroyAllWindows()