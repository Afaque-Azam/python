# write a list comprehension to print a list which contain table of a number entered by user

n = int(input("Enter a number :"))

table = [f"{n} x {i} = {n*i}" for i in range(1,11)]

print("\n".join(table))