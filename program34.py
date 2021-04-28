#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu




import pandas as pd
import matplotlib.pyplot as plt

inputFile = input('enter name for input file: ')

outputFile = input('Enter name for output file: ')


df = pd.read_csv(inputFile)

df["Date"] = pd.to_datetime(df["Date"].apply(str))

df["% Absent"] = df['Absent']/df['Enrolled']*100

df.plot(x = "Date", y = "% Absent")

plt.show()
plt.savefig(outputFile)

# 2018-2019_Daily_Attendance.csv