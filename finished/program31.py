#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

inputFile = input('enter name for input file: ')
outputFile = input('Enter name for output file: ')
homeless = pd.read_csv(inputFile)
#add the new column 'Fraction Children'
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
#plot fraction of children
homeless.plot(x = "Date of Census", y = "Fraction Children")
plt.show()
plt.savefig(outputFile)
