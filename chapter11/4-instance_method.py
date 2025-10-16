class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Name = {self.name}, Roll = {self.roll}")

s1 = Student("Afaque Azam", 20)

s1.show()