#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

homeless = pd.read_csv("DHS_Daily_Report.csv")
homeless.plot(x = "Date of Census", y = "Total Individuals in Shelter")
plt.show()
