class Person:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"Name = {self.name}")

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

    def showSalary(self):
        print(f"Name = {self.name}, Salary = {self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def showDepartment(self):
        print(f"Name = {self.name}, Salary = {self.salary}, Department = {self.department}")


m1 = Manager("Afaque Azam", 80000, "CSE")

m1.display()
m1.showSalary()
m1.showDepartment()