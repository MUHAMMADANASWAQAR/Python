# Variables
a, b = 3, 2

# 1. Arithmetic & Floor Division
print(f"Floor Division (3//2): {a // b}") # Output: 1

# 2. Assignment & Comparison (Not Equal: !=)
is_not_equal = (a != b)
print(f"Is a not equal to b? {is_not_equal}")

# 3. Logical Operators
# result: bool = a + b  <-- Yeh error dega kyunki 5 integer hai. Correct way:
result = bool(a + b) 
d = (a == b) and True
print(f"Logical AND result: {d}")

# 4. Membership Operators (Case Sensitive)
user_name = "Muhammad Anas Waqar"
result_in = "M" not in user_name  # False, kyunki 'M' wahan hai
print(f"Is 'M' NOT in user_name? {result_in}")

# 5. Identity Operators
# 'is' checks if they are the exact same object in memory
result_is = "Muhammad" is user_name 
print(f"Identity check: {result_is}")

# 6. Bitwise Operator (Example: AND)
# 3 is 011, 2 is 010. 3 & 2 = 010 (which is 2)
print(f"Bitwise AND (3 & 2): {a & b}")