# detect the spam message

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

msg = input("Enter your comment :")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("It is spam")

else:
    print("Not a Spam")