# write a program to open three text file if any these file are not present, a message without exiting the program must be printed prompting the same

try:
    with open("file1.txt", "r") as f:
        data = f.read()
        print(data)

except Exception as e:
    print(e)

try:
    with open("file2.txt", "r") as f:
        data = f.read()

except Exception as e:
    print(e)

try:
    with open("file3.txt", "r") as f:
        data = f.read()

except Exception as e:
    print(e)


print("Thank you")