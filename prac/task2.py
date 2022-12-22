import numpy as np
import cv2

cap = cv2.VideoCapture(0) #captures video from webcam, 0 is for the first/default one , use 1 or 2 .. for more webcams

while(True):
    ret, frame = cap.read()   # initiates an infinite loop, as long as return and frame is true 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #color from bgr to gray
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #will break the infinite loop if user presses 'q', checks every second
        break

cap.release()
cv2.destroyAllWindows()
