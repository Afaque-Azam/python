# create a class to store information of few programmers

class Programmer:
    company = "MicroSoft"

    def __init__(self, name, salary, city):
        self.name = name
        self.salary = salary
        self.city = city

o = Programmer("Nishu", 100000, "Delhi")

print(f"Company : {o.company}, Name : {o.name}, Salary : {o.salary}, City : {o.city}")


