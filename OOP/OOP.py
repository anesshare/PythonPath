#Objekat je paket varijabli i metoda koje se vezu za nesto npr za telefon noze bit isOn = true versionNumber = 13 itd
#klasa koristi za dizajn strukture objekta
from OOP.OOP2Eksterni import Car

bmw = Car(120,2007,"Black",False)
for key,value in bmw.__dict__.items():
    print(f"{key} {value}")
audi = Car(4,2020,"Blue",True)
for key,value in audi.__dict__.items():
    print(f"{key} {value}")
bmw.drive()
audi.stop()