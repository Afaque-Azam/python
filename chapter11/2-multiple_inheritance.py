# class Student:
#     def details(self,name,roll):
#         self.name = name
#         self.roll = roll

#         print(f"Name = {self.name}, Roll = {self.roll}")

# class Sports:
#     def activity(self,game):
#         self.game = game

#         print(f"Game = {self.game}")

# class Result(Student,Sports):
#     def score(self,marks):
#         self.marks = marks
#         print(f"Marks = {self.marks}")

# obj = Result()

# obj.details("Afaque Azam", 20)
# obj.activity("Cricket")
# obj.score(88)


class Father:
    def skils(self):
        print("Father:- Gardening, Teaching")

class Mother:
    def skils(self):
        print("Mother:- Cooking, Painting")

class Child(Father,Mother):
    def skils(self):
        print("child:- Coding, Dancing")
        Father.skils(self)
        Mother.skils(self)

c = Child()
c.skils()