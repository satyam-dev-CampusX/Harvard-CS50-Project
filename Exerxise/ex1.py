#wap to enter a 2 numbers and get all the calculations done on them
no_1= int(input("enter the first number: "))
no_2= int(input("enter the second number: "))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exponentiation")
print("6.modulus")
print("7.floor division")
ch = int(input("enter your choice: "))
if ch==1:
    print("addition of two numbers is:",no_1+no_2)
elif ch==2:
    print("subtraction of two numbers is:",no_1-no_2)
elif ch==3:
    print("multiplication of two numbers is:",no_1*no_2)
elif ch==4:
    print("division of two numbers is:",no_1/no_2)
elif ch==5:
    print("exponentiation of two numbers is:",no_1**no_2)
elif ch==6:
    print("modulud of two numbers is:",no_1%no_2)
elif ch==7:
    print("floor divisioin of two numbers is:",no_1//no_2)
else:
    print("Choose one of the above options")