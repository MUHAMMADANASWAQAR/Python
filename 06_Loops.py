count=1 #iterator
while count <=5 : 
  print("Hello World",count)
  count+=1
print("After Loop count value is ", count)  
# Multiplication table of n 
number= int(input("Enter a number to print its multiplication table : "))
count=1
while count < 11 :
  print(number,"*",count,"=",number*count)
  count+=1
# break and continue statement in while loop 
count=1 
while count <=10 : 
   if count % 2 ==0:
     count +=1
     continue
   print(count)
   count+=1
   
while(True):
    name=input("Enter your name : ")
    if name=="exit":
        print("Exiting the loop")
        break
    print("Hello ",name)
    
# For loop in python
for var in "anas":
    if var=="a":
        continue      
    print(var)
# range function in for loop (start, stop, step)
for i in range(1,11 , 2):
    print(i)  
count=0
word = "artificial "
for char in word : 
  if char=="i":
    count+=1
print("The number of i in the word is ", count)
#vowel count 
count=0
for char in word :
  if char=="i" or char=="a" or char=="e" or char=="o" or  char=="u" :
  #if char in "aeiou":  we can use this condition instead of above one
    count+=1
print("The number of vowel in the word is ", count)
# Sum of first n natural number
n=int(input("Enter a number to find the sum of first n natural number : "))
sum=0 
for i in range(1,n+1):
  sum+=i
print("The sum of first ",n," natural number is ", sum) 

