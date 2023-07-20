import cv2
import numpy as np


myimage = cv2.imread("kus.jpg" )

kesit = myimage[100:200, 100:200]

#kesiti sol ustteki koseye yapistiralim
myimage[0:100, 0:100] = kesit

myimage[0:100, 100:200] = kesit

myimage[100:200, 0:100] = kesit

#filtreleme

myimage[0:100, 0:100, 0] = 255 # blue

myimage[0:100, 100:200, 1] = 255 # green

myimage[100:200, 0:100, 2] = 255 # red

myimage[100:200, 100:200,] = 255 # all

myimage[100:200, 200:300, ] = (150, 150, 150)

#cv2.imshow("kesit", kesit)
cv2.imshow("image", myimage)

cv2.waitKey(0)
cv2.destroyAllWindows()