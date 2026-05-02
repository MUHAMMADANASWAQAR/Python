
f=open("simple.txt","w")
f.write(" this is over ride text")
f.close()
d=open("simple.txt","r")
data=d.readline()
print (data)
f.close()

