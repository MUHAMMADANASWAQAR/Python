num=[0,1,1,2,2,4,5]
i=0
for j in range(1,len(num)):
    if num[i]<num[j]:
        i=i+1
        num[i]=num[j]
for k in range(i+1):
    print(num[k])

print(i+1)