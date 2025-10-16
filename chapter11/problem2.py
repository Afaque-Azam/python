# create a class Pets from a class Animal and further create a class Dog from Pets and add method bark to class Dog

class Animal:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking")

class Pets(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Dog(Pets):
    def bark(self):
        print(f"{self.name} say Bow! Bow!")
        Animal.bark(self)
        Pets.bark(self)

d = Dog("daniel")
d.bark()