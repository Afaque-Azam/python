class Animal:
    species = "Mammel"

    def __init__(self,name):
        self.name = name

    def show(self):         # instance method
        print(f"Species = {self.name}")

    @classmethod
    def show2(cls):
        print(f"Species = {cls.species}")

a1 = Animal("Anaconda")

a1.show()
a1.show2()