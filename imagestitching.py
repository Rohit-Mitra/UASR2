import cv2
#import numpy as np

image_paths = ['uttower_left.jpg','uttower_right.jpg']              #accepts a list of images , have to change to make it accept more than 2 
imgs = [] 

for i in range(len(image_paths)):                                   #loop runs as long as image_paths has an image, ie returns true
	imgs.append(cv2.imread(image_paths[i]))
  
  
cv2.imshow('1',imgs[0])
cv2.imshow('2',imgs[1])                                             #need to change for more than 2


stitchy = cv2.Stitcher.create()
(dummy,output) = stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
  print("stitching ain't successful")                             #to check if the stitching procedure is successful 
                                                                  #.stitch() func returns a true value if stitching is succesful
else:
	print('Your Panorama is ready!!!')

# final output
cv2.imshow('final result',output)
cv2.waitKey(0)
cv2.destroyAllWindows()


#reference: https://www.geeksforgeeks.org/opencv-panorama-stitching/
