marks=[2,3,5,9,10]
print(len(marks))
print(marks[0])
print(marks[2:len(marks)])
print(marks[-5:-3])
#List is mutable in python
marks[0]=4
print(marks)
# methods in list 
marks.append(12)
print(marks)
marks.insert(2,6)
print(marks)
marks.remove(9)
print(marks)
marks.pop()
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)

part =marks.copy()
print(part)
marks.extend([15,20])
print(marks)
marks.index(5) # it will return the index of first occurrence of 5 in the list
print(marks.count(5)) # it will return the number of occurrence of 5 in
# List comprehension in python
squares =[x**2 for x in range(1,11)]
print(squares)
even_numbers=[x for x in range(1,21) if x%2==0]
print(even_numbers)
#List using for loop
x=[1,2,3,4,5]
index=0
for val in x: 
  if val==2:
    print(index)
    break
  index+=1