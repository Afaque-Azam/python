# snake water and gun game

'''

1 for snake
-1 for water
0 for gun

'''

import random

computer = random.choice([1, -1, 0])

youstr = input("Enter tour choice :")
youdict = {"s":1, "w":-1, "g":0}

reversedict = {1:"snake", -1:"water", 0:"gun"}

you = youdict[youstr]

print(f"Your choice is :{reversedict[you]}\nComputer choice is :{reversedict[computer]} ")




if(computer == you):
    print("its a draw.")

else:
    if(computer == 1 and you == -1):
        print("Computer Won.")

    elif(computer == 1 and you == 0):
        print("You won.")

    elif(computer == -1 and you == 1):
        print("You won.")

    elif(computer == -1 and you == 0):
        print("Computer won.")

    elif(computer == 0 and you == 1):
        print("Computer won.")

    elif(computer == 0 and you == -1):
        print("You won.")

    else:
        print("Something went wrong")