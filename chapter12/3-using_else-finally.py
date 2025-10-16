f = None
try:
    f = open("file1.txt", "r")
    data = f.read()

except FileNotFoundError:
    print("File not found!")

else:
    print('File read successfully!')
    print(f"File content :\n{data}")

finally:
    if f is not None:   # agar file open hogi to close hoga nahi to skip hoga
        f.close()     