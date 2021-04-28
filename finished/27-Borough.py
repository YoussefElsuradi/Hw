#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd


pop = pd.read_csv('nycHistPop.csv',skiprows=5)

mess, outp = input('Enter a Borough: '), input('Enter an Output name: ')



print(pop[mess].min())
print(pop[mess].max())
print(pop[mess].mean())
print(pop[mess].median())
print(pop[mess].std())

pop.plot(x="Year")

plt.imsave(outp, #idk wut to put in here)

plt.show()