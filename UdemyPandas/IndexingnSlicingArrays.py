import numpy as np
#Arr[0]- indexiranje
#Arr[:5] - primer slicing-a
#Arr[5::2] - Pocni od 5. elementa i uzmi svaki drugi

#Za dvodimenzionalne nizove:
#Arr[1,2]- Row index,Column index
arr = np.arange(12)
# print(arr[5:])  #daj mi od 5 do ostatka niza
# print(arr[:5]) #daj mi niz od pocetka do 5
newArr = arr.reshape(3,4)
print(newArr)
# print(newArr[:,:]) #Vraca sve
print(newArr[1:,:])
print(newArr[:,3]) #Vraca samo 3 kolonu
print(newArr[2,1]) #Vraca samo jedan element

#1. Zadatak
# IMAMO NIZ AGES TREBA DA POKAZEMO GRUPU GODINA IZ NIZA KORISTECI SLICING
ages = np.array([5, 10, 15, 19, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
youth_ages = ages[(ages >= 15) & (ages <= 19)]
adult_ages = ages[(ages >=20) & ( ages<=65)]
senior_ages=ages[(ages>=70)] #Prvo ide uslov za prvi deo pa onda za drugi deo
print(youth_ages)
print(adult_ages)
print(senior_ages)