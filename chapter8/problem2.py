# celcius to fahrenheit

def conversion(c):
    return (9/5) * c + 32

c = float(input("Enter temprature in celcius :"))

print("Temprature in fahrenheit is :",conversion(c))