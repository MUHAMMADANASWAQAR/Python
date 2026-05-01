class student :
  # class variable
 School="ABC School" 
 cgpa=3.5
 
 def __init__(self,name,subjects,department,cgpa):
   #instance variable
      self.name=name
      self.subjects=subjects
      self.department=department
      self.cgpa=self.cgpa #this one has more piority than class variable cgpa because we are using self.cgpa here
# total three methods in python class (instance method, class method and static method)
 @classmethod
 def get_school(cls):
  print("The school name is ", cls.School)
 @staticmethod
 def display_final_price(price ,discount):
  print(f"The Final price is {price-(discount*price/100)}")
  

def display(self):
  print("School:",self.School) # instance variable can access class variable using self
  print("Name:",self.name)
  print("Subjects:",self.subjects)
  print("Department:",self.department)
  print("CGPA:",self.cgpa) 
  
  
st1=student("Anas",["Math","Physics","Chemistry"],["Computer Science"],3.5)

st1.display_final_price(100 ,10 )
print(st1.name)
print(st1.subjects) 
#Example 
class product : 
  def __init__(self, name , price ):
    self.name=name 
    self.price=price 
    
  def get_info(self ):
    print (f" The name of the product {self.name} and price is this {self.price}" )

p1=product("shampoo" , 30)
p1.get_info()