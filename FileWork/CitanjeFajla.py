fP = "csvFile.csv"
import csv
try:
    with open(fP,"r") as file:
        content = file.read() #content = json.load(fP) za json fajl i printamo content[key]
        print(content)
        content2 = csv.reader(fP) #Za csv
        for line in content2:
            print(line,end="")
except FileNotFoundError:
    print("Not found on this location")