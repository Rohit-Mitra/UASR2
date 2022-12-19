import cv2
import os
import numpy as np
mainFolder = 'Images'
myfolders = os.listdir(mainFolder)
print(myfolders)

image_paths = []   #declare a list of images
imgs = [] 

for folder in myfolders:
    path = mainFolder + '/' + folder
    myList = os.listdir(path)
    print(f'Total no of images detected {len(myList)}')
    for imgN in myList:
        image_paths.append(f'{path}/{imgN}')

   

           
arr = np.array(image_paths)
for i in range(len(arr)):                                   #loop runs as long as image_paths has an image, ie returns true
	imgs.append(cv2.imread(arr[i]))
  
for i in range(len(arr)):
    cv2.imshow(f'{i}',imgs[i])                                            #need to change for more than 2


stitchy = cv2.Stitcher.create()
(dummy,output) = stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
  print("stitching ain't successful")                             #to check if the stitching procedure is successful 
                                                                  #.stitch() func returns a true value if stitching is succesful
else:
	print('Your stitched image is ready!!!')

# final output
cv2.imshow('final result',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

#reference: https://www.geeksforgeeks.org/opencv-panorama-stitching/
#https://www.youtube.com/watch?v=Z846tkgl9-U - module 9 for image stitching
