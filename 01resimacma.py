import cv2
import numpy as np
#resmi oku
image = cv2.imread("logo.png", 0) # 0: grayscale, 1: color 
# resmi kaydet
cv2.imwrite("logo_grayscale.png", image)

cv2.imshow("image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()