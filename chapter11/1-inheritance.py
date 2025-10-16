class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f"{self.name},Generic animal sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} say Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} say Meow!")

my_animal = Animal("Tiger")
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

print(my_animal.name)
print(my_dog.name)
print(my_cat.name)

my_animal.speak()
my_dog.speak()
my_cat.speak()