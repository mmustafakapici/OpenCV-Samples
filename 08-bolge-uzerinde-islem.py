import cv2
import numpy as np

myimage = cv2.imread("tablo.jpg" )
print(myimage.shape)


#resmin tam ortasini bulalim
ortax = int(myimage.shape[1]/2)
ortay = int(myimage.shape[0]/2)

#resmin ortasinda 50x50'luk bir bolge secelim
bolge = myimage[ortay-25:ortay+25, ortax-25:ortax+25]



#rectangle fonksiyonu ile bolgenin etrafina bir dikdortgen cizelim
cv2.rectangle(myimage, (ortax-25, ortay-25), (ortax+25, ortay+25), (0,255,0), 5)


#show
cv2.imshow("image", myimage)

#wait
cv2.waitKey(0)
cv2.destroyAllWindows()
