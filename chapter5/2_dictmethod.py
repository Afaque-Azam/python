marks = {
    "afaque": 98,
    "nishu": 87,
    "shanu": 37,
    1: "riju"
}

print(marks)

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"afaque":78 , "renuka" : 100})
print(marks)

print(marks.get("afaque")) 
print(marks["afaque"])

# print(marks.get("afaque1"))         none
# print(marks["afaque1"])             error