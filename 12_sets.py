# set={1, 2,2,2,2, }
# print(set) # set will only store unique values
# # set is mutable in python
# set.add(3)
# print(set)
# set.remove(2)
# print(set)
# set.discard(2) # it will not give an error if the element is not present
# print(set)
# print(len(set)) # length of the set
# # set operations    
# set1={1,2,3,4}
# set2={3,4,5,6}
# print(set1.union(set2)) # it will return a new set that contains all the elements from both sets
# print(set1.intersection(set2)) # it will return a new set that contains only the elements that are present in both sets
# print(set1.difference(set2)) # it will return a new set that contains only the elements that are present in set1 but not in set2
# print(set1.symmetric_difference(set2)) # it will return a new set that contains only the elements that are present in either set1 or set2 but not in both sets  
# # problem 
info= [("Anas", 25), ("Ali", 30), ("Ahmed", 35) , ("Anas", 25)]

# var_set =[]
# i=0
# for var in info:
#    var_set.insert(i,var[1])
#    i+=1
# print (set(var_set))
var_set=set()
for var in info:
   var_set.add(var[1])
print(var_set)
for va in info:
    if va[1] == 25:
        print(va[0])
        