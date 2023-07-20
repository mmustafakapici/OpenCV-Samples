import cv2
import numpy as np

myimage = cv2.imread("kus.jpg" ) 


# myimage[:,:,0] = 255 # BGR

# ortada bir kisima efekt uygulayalim
myimage[100:200, 100:200, 0] = 255

cv2.imshow("image", myimage)



cv2.waitKey(0)
cv2.destroyAllWindows()
