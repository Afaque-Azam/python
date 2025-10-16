t = (1,1,2,3,67,86,90,1,677.456)
T = (1,"harry",746)

print(t)

con = t + T
print(con)

no = t.count(1)
print(no)

i = t.index(1)
print(i)

print(min(t))

print(max(t))

print(2 in t)

print(746 in t)

print(len(t))

new = t[3:7]
print(new)


# packing unpacking
tuple = ("Afaque",23,"male")
name, age, gender = tuple
print(name,age,gender)