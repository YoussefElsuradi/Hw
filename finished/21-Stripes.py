#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


import matplotlib.pyplot as plt
import numpy as np

rows = int(input('How many rows of stripes do you want? '))
Stripes = np.ones((rows,rows,3))





Stripes[::2,:,0] = 0       

Stripes[1::2,:,1] = 0       


plt.imsave("out1.png", Stripes)
plt.imsave("out2.png", Stripes)