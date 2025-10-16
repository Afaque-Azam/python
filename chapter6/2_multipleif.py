age = int(input("Enter your age :"))

if(age % 2 == 0):
    print("Even")
    
if(age>=18):
    print("Ypu are adult.")

elif(age<0):
    print("Invalid age.")
    
else:
    print("You are child.")
