# Sum of two numbers using function
def sum(a,b): 
  return a+b
num1= int(input("Enter first number : "))
num2= int(input("Enter second number : "))
result= sum(num1,num2)
print("The sum of ",num1," and ",num2," is ", result)
# average of n numbers using function and also default parameter
def average(a , b , c=9):
  return (a+b+c)/3
result=average(10,20)
print("The average of 10, 20 and default value 9 is ", result)
#Types of function in python 
# 1. Built-in function : print(), input(), len() etc
# 2. User-defined function : sum(), average() etc
# 3. Anonymous function : lambda function
# Lambda function to find the square of a number
square = lambda x : x**2
num= int(input("Enter a number to find its square : "))
result=square(num)
print("The square of ",num," is ", result)  
a= lambda x, y : x+y
print("The sum of 5 and 10 is ", a(5,10))
# factorial of a number using function
def factorial(n):
  fact=1
  for i in range (1,n+1):
    fact *= i
  return fact
num= int(input("Enter a number to find its factorial : "))
print("The factorial of " ,num, "is ",factorial(num))
  
