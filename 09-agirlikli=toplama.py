import cv2
import numpy as np

image1 = cv2.imread("siyahbalon.jpg" )
image2 = cv2.imread("pembe.jpg" )

print(image1.shape)
print(image2.shape)

piksel1 = image1[100,100]
piksel2 = image2[100,100]


cv2.imshow("image1", image1)
cv2.imshow("image2", image2)

#agirlikli toplama
agirlikli_toplam = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

cv2.imshow("agirlikli toplam", agirlikli_toplam)


cv2.waitKey(0)
cv2.destroyAllWindows()