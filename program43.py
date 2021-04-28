#Youssef Elsuradi
#Youssef.elsuradi59@myhunter.cuny.edu

import folium
import pandas as pd

FileName = input("enter CSV File: ")
outputFile = input("enter output file name: ")


mapWorld = folium.Map(location=[40.768731,-73.964915],zoom_start=3)

df = pd.read_csv(FileName)

for index,row in df.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat,lon],popup=name)
    newMarker.add_to(mapWorld)
    
mapWorld.save(outfile=outputFile)
