from unittest import case

print("please choose following option")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exit")

print("please choose your option")

option=int(input())

print("enter 1st number")
num1=int(input())
print("enter 2nd number")
num2=int(input())

result=0
if option == 1:
 result=num1+num2
elif option == 2:
 result=num1-num2
elif option == 3:
 result=num1*num2
elif option == 4:
 result=num1/num2

print("result for given opeeration is::- ")
print(result)