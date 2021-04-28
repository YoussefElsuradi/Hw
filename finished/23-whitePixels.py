#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


import matplotlib.pyplot as plt
import numpy as np

ca = plt.imread(input('Enter file name: '))
plt.imshow(ca)
countSnow = 0  #variable for counting the white pixels in the image
t = 0.80

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
            countSnow +=1

print('Snow count is ',countSnow)