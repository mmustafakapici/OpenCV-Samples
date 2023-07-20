import cv2
import numpy as np

myimage = cv2.imread("tablo.jpg" )
print(myimage.shape)

#aynalama = reflect
aynaimage = cv2.copyMakeBorder(myimage,256, 256, 256, 256, cv2.BORDER_REFLECT)

#uzatma = replicate
uzatimage = cv2.copyMakeBorder(myimage,256, 256, 256, 256, cv2.BORDER_REPLICATE)

#tekrar = wrap
tekrarimage = cv2.copyMakeBorder(myimage,256, 256, 256, 256, cv2.BORDER_WRAP)

#siyah = constant
siyahimage = cv2.copyMakeBorder(myimage,10, 10, 10, 10, cv2.BORDER_CONSTANT, value = [0,0,0])

#cerceve = isim
cerceveimage = cv2.copyMakeBorder(myimage,10, 10, 10, 10, cv2.BORDER_ISOLATED)

cv2.imshow("image", myimage)
cv2.imshow("ayna", aynaimage)
cv2.imshow("uzat", uzatimage)
cv2.imshow("tekrar", tekrarimage)
cv2.imshow("siyah", siyahimage)
cv2.imshow("cerceve", cerceveimage)

cv2.waitKey(0)
cv2.destroyAllWindows()