# The perfect guess :- we are going to write a program that generates a random number and ask the user to get it

import random

n = random.randint(1,100)

guesses = 1
a = 0
while(a != n):
    a = int(input("Guess the number :"))

    if(a > n):
        print("Lower number please.")
        guesses += 1

    elif(a < n):
        print("Higher number please")
        guesses += 1

print(f"You have Guessed that number {n} in {guesses} attempt")
