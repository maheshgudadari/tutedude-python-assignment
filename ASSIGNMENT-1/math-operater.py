from unittest import case

print("please choose following option")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exit")

option=int(input("please choose your option::"))

num1=int(input("enter 1st number::"))
num2=int(input("enter 2nd number::"))

result=0
if option == 1:
 result=num1+num2
elif option == 2:
 result=num1-num2
elif option == 3:
 result=num1*num2
elif option == 4:
 result=num1/num2

print("result for given opeeration is::- ", result)

# Task 2: Create a Personalized Greeting
fName=input("enter your first name:")
lName=input("enter your last name:")

print('Hello,',fName +' '+ lName + ' ! welcome to the Python program.')