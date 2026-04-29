class student:
   def __init__():
     print("This is a  default constructor") # in python we can use only one constructor in a class and also if we have two constructor mean last constructor will override the first one
     
   def __init__ (self, name, subjects, department,cgpa):
      self.name=name
      self.subjects=subjects
      self.department=department
      self.cgpa=cgpa
      
s1=student("Anas",["Math","Physics","Chemistry"],["Computer Science"],3.5 )
print(s1.name)
print(s1.subjects)
print(s1.department)
print(s1.cgpa)

