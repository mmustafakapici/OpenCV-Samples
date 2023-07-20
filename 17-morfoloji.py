import cv2
import numpy as np


image= cv2.imread("tablo.jpg")

kernel = np.ones((5,5),np.uint8)

# Erosion
erosion = cv2.erode(image,kernel,iterations = 1)

# Dilation
dilation = cv2.dilate(image,kernel,iterations = 1)
dilation2 = cv2.dilate(image,kernel,iterations = 2)

# Opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Top Hat
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Black Hat
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original",image)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Dilation2",dilation2)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.imshow("Gradient",gradient)
cv2.imshow("Top Hat",tophat)
cv2.imshow("Black Hat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()

