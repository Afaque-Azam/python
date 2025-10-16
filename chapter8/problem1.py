# greatest of three

def greatest(a,b,c):
    return max(a,b,c)

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

print(f"The greatest number is : {greatest(a,b,c)}")