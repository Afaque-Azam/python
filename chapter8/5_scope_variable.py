a = 199   #global variable

def fun():
    a = 7   # local variable
    print(a)

fun()
print(a)

# using the global keyword modify the global variable inside function

b = 199    # global variable
 
def fun1():
    global b
    b = 7    # modifie the global variable
    print(b)

fun1()
print(b)
