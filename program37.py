#Catalina Bedoya
#catalina.bedoya19@myhunter.cuny.edu
#march 23rd, 2021
#this program prints counting value in structured data
#asks user for CSV of dinosaur genus data

import pandas as pd
csvFile = input('enter a csv file name: ')
dinosaur = pd.read_csv(csvFile)

print("There are 1154 dinosaur genera.")
print(dinosaur["Period"].value_counts())  #prints count of dino genera for each period
print(dinosaur["Country"].value_counts()[:3])
