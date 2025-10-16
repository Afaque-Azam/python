# polymorphism(one name, many forms) with function and object

class Dog:
    def sound(self):
        return "Bark"
    
class Cat:
    def sound(self):
        return "Meow"


for animal in (Dog(), Cat()):
    print(animal.sound())



# polymorphism with inheritance (Method Overriding)

class Birds:
    def intro(self):
        print("I am a Bird") 
    
    def fly(self):
        print("Some birds can fly")
    
class Penguin(Birds):
    def fly(self):
        print("Penguins can not fly")
        Birds.intro(self)
    
b = Birds()
p = Penguin()

b.fly()
p.fly()