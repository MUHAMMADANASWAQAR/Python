
f=open("simple.txt","w")
f.write(" this is over ride text")
f.close()
d=open("simple.txt","r")
data=d.readline()
print (data)
f.close()
#using with fo open the file 
with open("simple.txt",'r') as f : 
  print(f.read())

  
# import os 
# os.remove("simple2.txt")

#File operation 
# reading [default ]
# writing and truncate 
# writing and append 
with open("simple.txt" , "a") as d : 
  d.write("\n Appended new text ")
# create new and open for writing 
# binary mode audio , vedio
# text mode 
# open disk file for update (r&w) we have + r+ fromstarting its overwrite not all  a+ write from last  w+  override all text 
