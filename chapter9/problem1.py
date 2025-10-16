# check any word present in the file

f = open("poem.txt")

content = f.read()

if("twinkle" in content):
    print("Yes present")

else:
    print("Not present")

f.close()