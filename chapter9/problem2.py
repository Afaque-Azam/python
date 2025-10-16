# hiscore.txt which is either blank or contains the previous hiscore
# write program to update a hiscore whenever game() function breaks the hiscore

import random


def game():
    print("You are playing...")
    score = random.randint(1,100)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore == ""):
            hiscore = 0
        else:
            hiscore = int(hiscore)

    print(f"Your score is : {score}")
    if(score > hiscore):
        print("New high score.")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))


game()

