import cv2
import numpy as np

image = cv2.imread("tablo2.png",)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged

wide = cv2.Canny(blur, 10, 200)
tight = cv2.Canny(blur, 225, 250)
edged = auto_canny(blur)

cv2.imshow("Original", image)
cv2.imshow("blur", blur)
cv2.imshow("Edges", np.hstack([wide, tight, edged]))

cv2.waitKey(0)
cv2.destroyAllWindows()