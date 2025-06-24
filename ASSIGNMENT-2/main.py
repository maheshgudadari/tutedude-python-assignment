
# Control Structures in Python
# Task 1: Check if a Number is Even or Odd

num1=int(input("enter first number::"))

if num1%2==0:
    print(num1," is an even number")
else:
    print(num1," is an odd number")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
sum=0;
num2= range(0,51)
for num in num2:
    sum=sum+num
print("The sumof numbers from 1 to 50 is:",sum)