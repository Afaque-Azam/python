# # greatest of three
# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))
# c = int(input("Enter third number :"))

# if(a>b):
#     if(a>c):
#         print("a is greatest")
#     else:
#         print("c is greatest")  

# else:         
#     if(b>c):
#         print("b is greatest")
#     else:
#         print("c is greatest")


# greatest of four

a1 = int(input("Enter first number :"))
b1 = int(input("Enter second number :"))
c1 = int(input("Enter third number :"))
d1 = int(input("Enter fourth number :"))

if(a1>b1 and a1>c1 and a1>d1):
    print("greatest number is :",a1)

elif(b1>a1 and b1>c1 and b1>d1):
    print("greatest number is :",b1)

elif(c1>a1 and c1>b1 and c1>d1):
    print("greatest number is :",c1)

else:
    print("greatest is :",d1)