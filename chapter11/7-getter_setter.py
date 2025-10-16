class Student:
    def __init__(self,name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
    def set_marks(self,new_marks):
        self.__marks = new_marks


s1 = Student("Afaque Azam",89)

print(s1.name)
print(s1.get_marks())

s1.set_marks(98)
print(s1.get_marks())