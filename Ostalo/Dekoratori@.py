#Dekoratori jeste dodavanje neke orginalne funkcije bez da se njeno orginalno stanje menja

def dodajPreliv(func):
    def wrap():
        print("Dodali ste preliv!")
        func()
    return wrap     #neki sablon za kreiranje dekoratora
#ako nema ovoga wrapa, svaki put ce se pozvat getsladoled funkcija jer se poziva uvek kad se pozove i dodajpreliv, a wrapper se koristi da se ona pozove kad se glavna...
#...funkcija pozove

@dodajPreliv
def getSladoled():
    print("Izvoli sladoled")
getSladoled()