# create a class Employee and add salary and increment property to it 
# write a method salary-after-increment with @property decorator with a setter which change the value of increment based on the salary

class Employee:
    salary = 20000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary/self.salary)-1) * 100

e = Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 2500
print(e.increment)