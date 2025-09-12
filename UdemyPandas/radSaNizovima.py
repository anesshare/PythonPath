import numpy as np  
from numpy.random import default_rng
# myList = [x* 10 for x in range(1,11)]
# myArr = np.array(myList).reshape(10,1)
# print(myArr)
##############################################

#Kreiranje nizova

# ones = np.ones(2,dtype="int") #Pravi niz s jedinicama
# print(ones)
# zeros = np.zeros(100,"int") #Pravi niz s nulama
# print(zeros)
# print(np.arange(10).reshape(5,2)) #Kao petlja ide od 0-9 plus reshape daj mi 2 kolonei 5 redova
# linsp = np.linspace(8,64,8) #Idi od A -> B i povecavaj mi vrednost za X
# print(linsp)
###############################################

#Random number generator

# rng = default_rng(10)
# randArr = rng.random(10) #12345 vraca niz od 5 random brojeva ako se stavi 5 onda se daje 5 uvek istih vrednosti
# print(randArr)
# print(rng.normal(50,5,10))#50 - srednja vrednost 5-Std Devijacija 10-Kolicina brojeva 
#                             #Std devijacija jeste koliko se vrednosti rasipaju oko prosecne vrednosti u ovom slucaju koliko se 5 prosipa oko 50
##############################################################################

#1.Napravi mi niz od 10-100 i nek ima 5 redova i 5 kolona
niz = np.linspace(10,100,10).reshape(5,2)
print(niz)
#2. Nakon toga daj mi niz ranodm brojeva od 0-1 i nek budu 3x3 
rng = default_rng(10)
randArr = rng.random(9).reshape(3,3)
print(randArr)