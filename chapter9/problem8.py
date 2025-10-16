# check both file are identical or not

with open("file1.txt") as f:
    content1 = f.read()

with open("poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes, both files are identical")

else:
    print("No, it is not identical")