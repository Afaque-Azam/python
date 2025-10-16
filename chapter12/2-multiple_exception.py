try:
    a = int(input("enter a Number :"))
    result = 10/a
    print(result)
    
except ZeroDivisionError:
    print("You can not devide by zero.")

except ValueError:
    print("Invalid input!, please enter a number.")

