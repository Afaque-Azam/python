# star pattern
'''
    *
   ***
  *****
 *******
*********

'''

# n = int(input("Enter a number :"))

# for i in range(1,n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1))
 
'''
*
**
***
****

'''
# n = int(input("Enter a number :"))

# for i in range(1,n+1):
#     print("*" * i)


'''

****
*  *
*  *
****

'''

n = int(input("Enter a number :"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if(j == 1 or j == n or i == 1 or i == n):
            print("*", end="")
        else:
            print(" ",end="")

    print("")