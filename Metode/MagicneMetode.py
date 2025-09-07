# __ovemetode__
class Book:
    def __init__(self,title,author,numPages): #Magicna metoda 
        self.title = title
        self.author = author
        self.numPages = numPages
#Kad se pozove init metoda i pozove u print objekat, on smao pokazuje adresu ali ne ivrednosti
    def __str__(self):  #Kad se ova metoda doda, bez poziva se aktivira i ona pokazuje direktno vrednosti u printu
        return f"{self.title} {self.author} {self.numPages}"
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author #eq metoda za proveru equality za objekte
book1 = Book("Hobbit","JRR","310")
book2 = Book("HarryPotter","JKROWLING","223")
book3 = Book("Lion","Ivo Andric","622")
book4 = Book("Lion","Ivo Andric","622")

print(book1)
print(book2)
print(book3)
print(book3 == book4) #Primer __eq__ izvrsavanja
#MagicMetode ili thundermethods su metode koje se ne pozivaju odvojeno, vec sto se pozove objekat ono povlaci ove funkcije iz klase na osnovu koje je objekat napravljen