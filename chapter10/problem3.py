# create a class which has method 
import random

class Rail:
    def __init__(self, tno):
        self.tno = tno
        
    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.tno} From {fro} To {to}")

    def status(self):
        print(f"Train no {self.tno} is running on time")

    def fare(self, fro, to):
        print(f"Ticket fare in train no {self.tno} From {fro} To {to} is {random.randint(222,5555)}") 

r = Rail(12510)

r.book("Bettiah", "Delhi")
r.status()
r.fare("Bettiah", "Delhi")