# check in which line python is present

with open("problem6.txt") as f:
    lines = f.readlines()

linenumber = 1
for line in lines:
    if "python" in line:
        print(f"Yes python is present in line number : {linenumber}")
        break
    linenumber += 1

else:
    print("No python is not present")