import numpy as np
import cv2 as cv

image = cv.imread('me.jpg')
# cv.imshow('Original',image)
# cv.waitKey(0)

# convert image into grayscale
def ApplyGrayImage(image):
    gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    
    # cv.imshow('Grayscale',gray_image)
    # cv.waitKey(0)
    return gray_image
    
grayImage = ApplyGrayImage(image)
# cv.imshow('Grayscale',grayImage)
# cv.waitKey(0)

# apply guassian filter using 3x3 grid to help reduce the amount of noise in image
kernel = np.ones((5,5),np.float32)/25
blur_image = cv.filter2D(grayImage,-1,kernel)
# cv.imshow('Blur',blur_image)
# cv.waitKey(0)

edgeDetection = cv.Canny(grayImage,75,200)
cv.imshow('edgeDetection',edgeDetection)
cv.waitKey(0)
