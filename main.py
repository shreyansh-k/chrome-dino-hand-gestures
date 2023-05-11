# https://github.com/Sandeep-Sthapit/HandGestureDetection

import cv2
import pyautogui

rpalm_cas = cv2.CascadeClassifier('rpalm.xml')

cap = cv2.VideoCapture(0)
count=0

print('Start Now!')

while 1:
    ret, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rpalm = rpalm_cas.detectMultiScale(gray, 1.1, 4)
    
    for (x,y,w,h) in rpalm:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if len(rpalm) > 0:
            count=count+1
            # time.sleep(0.5)
            print("Palm detected",count)
            pyautogui.press('space')
    
    cv2.imshow('img',img)
    #press esc key to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

#open chrome dino by:
#chrome://dino
#chrome://network-error/-106