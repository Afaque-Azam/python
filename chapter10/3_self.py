class Employee:
    lang = "Python"
    salary = 120000

    def getInfo(self):
        print(f"Language : {self.lang}, Salary : {self.salary}")

    def greet(self):       #self parameter
        print("Good Morning")

    @staticmethod          # static method
    def greet2():
        print("Thank You")

afaque = Employee()

afaque.greet()
afaque.getInfo()
afaque.greet2()
