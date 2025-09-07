class Animal:
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")
class Prey(Animal):         #Cak i glavne klase mogu da imaju inheritance
    def flee(self):
        print("This animal is fleeing")
class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
hawk.hunt()
hawk.sleep()    #Ovde se vidi da cak i pod pod klasa moze od parent klase da uzima metode
fish.hunt()
fish.flee()
