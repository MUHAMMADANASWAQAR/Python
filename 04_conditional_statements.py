a=input()
if a=="red":
  print("The color is red")
elif a=="blue":
  print("The color is blue")
else :
  print("The Select color is neither blue nor red ")
  
# number is multiply by 5 or not 
number=int(input("Enter a number to check if it is multiply by 5 or not : "))
if number%5==0:
  print("The number is multiply by 5")
else : 
  print("The number is not multiply by 5")
  
  # number is evern or not 
number=int(input("Enter a number to check if it is even or not : "))  
if number%2==0:
    print("The number is even")
else :
    print("The number is odd")
# Nesting of if statement
Name=input("Enter your name : ")
password=input("Enter your password : ")
if Name=="admin" and password=="admin123":
    print(" Login Successfully ")
else :
    if Name!="admin":
        print("Invalid Name")
    else: 
        print("Invalid Password")
  