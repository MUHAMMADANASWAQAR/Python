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