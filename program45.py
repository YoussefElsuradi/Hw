#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


import folium
import pandas as pd

FileName = input("Please enter the name of the input file: ")
outputFile = input("Please enter the name of the output file: ")
borough = input("Please enter the name of the borough: ")


mapWorld = folium.Map(location=[40.768731,-73.964915],zoom_start=3)

df = pd.read_csv(FileName)

df = df.groupby(['Borough']).get_group(borough)

for index,row in df.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Borough"]
    newMarker = folium.Marker([lat,lon],popup=name)
    newMarker.add_to(mapWorld)
    
mapWorld.save(outfile=outputFile)
