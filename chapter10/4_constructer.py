class Employee():
    lang = "Python"
    salary = 120000

    def __init__(self, name, lang, salary):   # dunder method 
        self.name = name
        self.lang = lang
        self.salary = salary

    def getInfo(self):
        print(f"Name: {self.name}, Language : {self.lang}, Salary : {self.salary}")


afaque = Employee("Afaque", "JavaScipt", 130000)

afaque.getInfo()

