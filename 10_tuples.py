# tuples are immutable data structures that can hold a collection of items. They are similar to lists but cannot be modified after they are created. Tuples are defined using parentheses () and can contain elements of different data types.
# Creating a tuple
my_tuple = (1, "Hello", 3.14, [1, 2, 3])
print(my_tuple) 
# Accessing elements of a tuple
print(my_tuple[0])
print(my_tuple[1:3])
# Tuples are immutable, so we cannot modify them directly. However, we can create a new tuple by concatenating existing tuples.
new_tuple = my_tuple + (4, 5, 6)    
print(new_tuple)
print(my_tuple[3][1]) # accessing the element 3 from the list inside the tuple
print(len(my_tuple)) # length of the tuple