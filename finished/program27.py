#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu
import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)

borough = input('Enter a borough name: ')
file = input('Enter a file name: ')


print("the minimum number living in this borough is", pop[borough].min())
print(" the maximum # living here is", pop[borough].max())
print(" the average # living here is", pop[borough].mean())
print("median number living here is", pop[borough].median())
print("std living here is", pop[borough].std())

pop['Fraction'] = pop[borough]/pop['Total']

pop.plot(x = "Year", y = "Fraction")

fig = plt.gcf()
fig.savefig(file)

