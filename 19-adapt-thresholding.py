import cv2
import numpy as np
# Load the image

image = cv2.imread("tablo2.png" ,0 )
image2 = cv2.imread("tablo.jpg" ,0 )
image3 = cv2.imread("opencv.jpg" ,0 )
image4 = cv2.imread("pythonlogo.jpg" ,0 )

#thresholding ile blur fotoyu daha iyi görebiliriz


# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
thresh2 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
thresh3 = cv2.adaptiveThreshold(image3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
thresh4 = cv2.adaptiveThreshold(image4, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)

#gaussian thresholding
thresh5 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
thresh6 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
thresh7 = cv2.adaptiveThreshold(image3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
thresh8 = cv2.adaptiveThreshold(image4, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)

# otsu
ret,thresh9 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh10 = cv2.threshold(image2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh11 = cv2.threshold(image3,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh12 = cv2.threshold(image4,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Show the images numpy vertical stack
cv2.imshow("Originals", np.vstack([image, image2, image3, image4]))
cv2.imshow("Mean", np.vstack([thresh, thresh2, thresh3, thresh4]))
cv2.imshow("Gaussian", np.vstack([thresh5, thresh6, thresh7, thresh8]))
cv2.imshow("Otsu", np.vstack([thresh9, thresh10, thresh11, thresh12]))



cv2.waitKey(0)

cv2.destroyAllWindows()


