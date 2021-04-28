#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


import pandas as pd

file = input('Enter a file name: ')
pop = pd.read_csv(file)

rock_types = pop.groupby('Dominant Rock Type')

#print(" average elevation for each Dominant Rock Type is", pop.rock_types.mean())


print(rock_types["Elevation (Meters)"].mean())

italy = pop.groupby("Country").get_group('Italy')

print('The tallest Volcaon in italy is: ', italy['Elevation (Meters)'].max())