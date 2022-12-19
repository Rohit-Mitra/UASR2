import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('testimage.jpg',cv2.IMREAD_GRAYSCALE) #reads image and turns it into all gray pixels
cv2.imshow('image',img) #prints the image
cv2.waitKey(0)
cv2.destroyAllWindows()
