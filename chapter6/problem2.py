# pass or fail 

m1 = int(input("Enter first marks :"))
m2 = int(input("Enter second marks :"))
m3 = int(input("Enter third marks :"))

per = (m1 + m2 + m3)/3

if(per>=40 and m1>=33 and m2>=33 and m3>=33):
    print("Student passed :",per)

else:
    print("Student failed :",per)