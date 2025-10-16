# try:
#     a = int(input("Enter a number :"))
#     print(a)
# except Exception as e:
#     print(e)

# print("Succesfully")

try:
    a = 10/0
    print(a)

except Exception as e:
    print(e,"not possible")