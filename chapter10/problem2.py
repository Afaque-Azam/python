# create a class capable of finding square cube and squareroot

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square : {self.n * self.n}")

    def cube(self):
        print(f"Cube : {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"Squareroot : {self.n ** 1/2}")

c = Calculator(4)

c.square()
c.cube()
c.squareroot()