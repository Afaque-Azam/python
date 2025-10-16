class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,new_marks):
        self.__marks = new_marks

s1 = Student("Afaque Azam",87)

print(s1.name)

print(s1.marks)

s1.marks = 50

print(s1.marks)