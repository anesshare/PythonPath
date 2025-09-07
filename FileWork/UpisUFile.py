import os
import json
import csv
employee = {
    "name": "John Doe",
    "age": 30,
    "job": "Software Engineer"
}
csvEmployee = [["Name,Age,Job"],["Anes",30,"cook"],["Patrick",37,"Unemployed"],["John",45,"Software Engineer"]]
filePath = "text.txt"
with open(filePath,"w") as file:        #Za pisanje u fajl #ako umesto W stavimo X ono ga napravi novi fajl i ispise
    json.dump(employee, file,indent=4)            #json dump pretvara python objekat u json objekat i automatski ga upisuje u fajl #indent 4 dodaje uvlačenje radi čitljivosti
    print(f"txt file {filePath} was created!")

with open("csvFile.csv", "w") as file:  #Za pisanje u csv fajl
    writer = csv.writer(file)            #csv writer pretvara python objekat u csv objekat i automatski ga upisuje u fajl
    for row in csvEmployee:
        writer.writerow(row)
    print(f"csv file csvFile.csv was created!")

