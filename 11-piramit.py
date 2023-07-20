import cv2
import numpy as np

image=cv2.imread("tablo.jpg")
print(image.shape)

#2 kat büyüt
image2=cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
print(image2.shape)

#2 kat küçült
image3=cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
print(image3.shape)

cv2.imshow("real",image)
cv2.imshow("image2",image2)
cv2.imshow("image3",image3)

cv2.waitKey(0)
cv2.destroyAllWindows()
