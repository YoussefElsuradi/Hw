#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

inputFile = input('Enter a csv file name: ')
outputFile = input('Enter name for output file: ')
pop = pd.read_csv(inputFile)

groupedData = pop.groupby('neighbourhood_group')['price'].mean()


groupedData.plot.bar()
plt.xlabel('Borough')
plt.ylabel('Average Price')

plt.gcf().subplots_adjust(bottom=0.25)
fig = plt.gcf()
fig.savefig(outputFile)
