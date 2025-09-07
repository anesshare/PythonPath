class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def bark(self):
        print("WOOF")

class Cat(Animal):
    def meow(self):
        print("MEOW")
class Mouse(Animal):
    def speak(self):
        print("HEHE")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")
print(dog.name)
print(dog.isAlive)
dog.eat()
dog.sleep()
dog.bark()
cat.meow()
mouse.speak()