'''
Created on Nov. 1, 2022

@author: dancrha

References:
https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
'''

import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('cntower.jpeg',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Detected Image'), plt.xticks([]), plt.yticks([])
plt.show()

