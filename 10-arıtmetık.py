import cv2
import numpy as np

image=cv2.imread("kus.jpg")

#gray
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print(image.shape)
print(gray.shape)

#kolay
image_gray=cv2.imread("kus.jpg",0)
print(image_gray.shape)


cv2.imshow("real",image)
cv2.imshow("gray",gray)
cv2.imshow("image_gray",image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()