def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    
    return "Access granted"

try:
    print(check_age(20))
    print(check_age(12))

except ValueError as e:
    print("Error :", e)