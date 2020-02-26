import cv2
import numpy as np 

kamera=cv2.VideoCapture(0)
dusuk=np.array([20,30,30])
yuksek=np.array([50,255,255])

while True:
    ret,kare=kamera.read()
    hsv=cv2.cvtColor=(kare,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,dusuk,yuksek)
    resim=cv2.bitwise_and(kare,kare,mask=mask)
    
    
    cv2.imshow("Hsv",hsv)
    cv2.imshow("resim",resim)
    cv2.imshow("Kamera",kare)
    
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
    
kamera.release()
cv2.destroyAllWindows()
