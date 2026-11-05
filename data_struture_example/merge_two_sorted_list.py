list1=[1,2,3,0,0,0]
list2=[2,5,6]  
m=3
n=3
i=m-1
j=n-1
x=m+n-1

while i>=0 and j>=0:
    if list1[i]>list2[j]:
        list1[x]=list1[i]
        i=i-1
        x=x-1
        
    else:
        list1[x]=list2[j]
        j=j-1
        x=x-1

while(j>=0):
     list1[x]=list2[j]
     j=j-1
     x=x-1

print(list1)



