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


"""
#for recording video we can do:
import numpy as np
import cv2

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
"""
