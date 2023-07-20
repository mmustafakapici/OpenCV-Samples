import cv2
import numpy as np

image=np.zeros((512,512,3),np.uint8)


cv2.line(image,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(image,(384,0),(510,128),(0,255,0),3)
cv2.circle(image,(447,63),63,(0,0,255),-1)
cv2.ellipse(image,(256,256),(100,50),0,0,180,255,-1)

#metin
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,"OpenCV",(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

#goster
cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
