import cv2
import numpy as np

# Load the image

image = cv2.imread("tablo2.png" ,0 )
image2 = cv2.imread("tablo.jpg" ,0 )
image3 = cv2.imread("opencv.jpg" ,0 )
image4 = cv2.imread("pythonlogo.jpg" ,0 )

# simple thresholding

ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(image3, 200, 255, cv2.THRESH_BINARY)
ret, thresh4 = cv2.threshold(image4, 220, 255, cv2.THRESH_BINARY)

ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh6 = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh7 = cv2.threshold(image3, 200, 255, cv2.THRESH_BINARY_INV)
ret, thresh8 = cv2.threshold(image4, 220, 255, cv2.THRESH_BINARY_INV)

ret, thresh9 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thresh10 = cv2.threshold(image2, 127, 255, cv2.THRESH_TRUNC)
ret, thresh11 = cv2.threshold(image3, 200, 255, cv2.THRESH_TRUNC)
ret, thresh12 = cv2.threshold(image4, 220, 255, cv2.THRESH_TRUNC)

ret, thresh13 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thresh14 = cv2.threshold(image2, 127, 255, cv2.THRESH_TOZERO)
ret, thresh15 = cv2.threshold(image3, 200, 255, cv2.THRESH_TOZERO)
ret, thresh16 = cv2.threshold(image4, 220, 255, cv2.THRESH_TOZERO)

ret, thresh17 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
ret, thresh18 = cv2.threshold(image2, 127, 255, cv2.THRESH_TOZERO_INV)
ret, thresh19 = cv2.threshold(image3, 200, 255, cv2.THRESH_TOZERO_INV)
ret, thresh20 = cv2.threshold(image4, 220, 255, cv2.THRESH_TOZERO_INV)


# vstack stacks arrays in sequence vertically (row wise).
cv2.imshow("Originals", np.vstack([image, image2, image3, image4]))
cv2.imshow("Binary", np.vstack([thresh1, thresh2, thresh3, thresh4]))
cv2.imshow("Binary Inv", np.vstack([thresh5, thresh6, thresh7, thresh8]))
cv2.imshow("Trunc", np.vstack([thresh9, thresh10, thresh11, thresh12]))
cv2.imshow("To Zero", np.vstack([thresh13, thresh14, thresh15, thresh16]))
cv2.imshow("To Zero Inv", np.vstack([thresh17, thresh18, thresh19, thresh20]))


#adaptif thresholding

cv2.waitKey(0)

cv2.destroyAllWindows()


