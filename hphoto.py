# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:48:13 2021

@author: Herr
"""
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from skimage.io import imread

image1 = imread('hockeyimg.gry.png')
n_rows, n_cols, color = image1.shape

Gx = np.array([[-1,0,-1], [-2,0,2], [-1,0,1]])
Gy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])


newimg1 = np.zeros(image1.shape)
newimg2 = np.zeros(image1.shape)
newimg3 = np.zeros(image1.shape)
newimg4 = np.zeros(image1.shape)


for i in range(n_rows):
   newimg1[i,:,:] = signal.convolve(image1[i,:,:], Gx,'same')
   
for j in range(n_cols):
   newimg2[:,j,:] =  signal.convolve(image1[:,j,:], Gx,'same')
   
for i in range(n_rows):
   newimg3[i,:,:] = signal.convolve(image1[i,:,:], Gy,'same')
   
for j in range(n_cols):
   newimg4[:,j,:] =  signal.convolve(image1[:,j,:], Gy,'same')


plt.figure()
plt.imshow(newimg1,'gray')
plt.title('convol along rows gx')

plt.figure()
plt.imshow(newimg2,'gray')
plt.title('convol along cols gx')


plt.figure()
plt.imshow(newimg3,'gray')
plt.title('convol along cols gy')

plt.figure()
plt.imshow(newimg4,'gray')
plt.title('convol along cols gy')


plt.figure()
plt.imshow(image1)

