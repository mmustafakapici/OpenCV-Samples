import cv2


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    #text
    font=cv2.FONT_HERSHEY_SIMPLEX
    text = "Software"
    cv2.putText(frame,text,(10,100),
    font,1,(100,100,100),4,cv2.LINE_AA)

    cv2.imshow("frame",frame)


    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
