# check username contain less than 10 char

user_name = input("Enter the user name :")

length = len(user_name)

if(length<=10):
    print("valid username")

else:
    print("invalid username")