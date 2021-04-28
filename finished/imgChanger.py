#Name:  Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


pic = input('Enter a PNG file: ')

img = plt.imread(pic)   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
                        

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0             #should take out the red from the img


plt.imshow(img2)         #Load our new image into pyplot
#plt.show()               #Show the image (waits until closed to continue)

    
plt.imsave('out1.png' , img2)  #Save the image we created to the file:
plt.imsave('out2.png' , img2)  #Save the image we created to the file:
# csBridge.png