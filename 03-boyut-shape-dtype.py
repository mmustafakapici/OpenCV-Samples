import cv2
import numpy as np
#resmi oku
image = cv2.imread("kus.jpg" ) # 0: grayscale, 1: color 

cv2.imshow("image", image)

print(image)

#shape
print('shape:',image.shape)

#boyut
print('boyut:',image.size)

#veri tipi
print('veri tipi:',image.dtype)

cv2.waitKey(0)

cv2.destroyAllWindows()