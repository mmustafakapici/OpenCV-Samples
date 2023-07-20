import cv2
import numpy as np

image = cv2.imread("gurultulu_buyuk.png")
#resize
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)


#mean filter
mean3 = cv2.blur(image,(3,3))
mean5 = cv2.blur(image,(5,5))
mean7 = cv2.blur(image,(7,7))

#median filter
median3 = cv2.medianBlur(image,3)
median5 = cv2.medianBlur(image,5)
median7 = cv2.medianBlur(image,7)

#gaussian filter
gaussian3 = cv2.GaussianBlur(image,(3,3),0)
gaussian5 = cv2.GaussianBlur(image,(5,5),0)
gaussian7 = cv2.GaussianBlur(image,(7,7),0)

#bilateral filter
bilateral9 = cv2.bilateralFilter(image,9,75,75)
bilateral11 = cv2.bilateralFilter(image,11,100,100)
bilateral13 = cv2.bilateralFilter(image,13,125,125)

cv2.imshow("image",image)
cv2.imshow("means",np.hstack([mean3,mean5,mean7]))
cv2.imshow("medians",np.hstack([median3,median5,median7]))
cv2.imshow("gaussians",np.hstack([gaussian3,gaussian5,gaussian7]))
cv2.imshow("bilaterals",np.hstack([bilateral9,bilateral11,bilateral13]))




cv2.waitKey(0)
cv2.destroyAllWindows()