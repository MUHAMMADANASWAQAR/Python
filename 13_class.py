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
  
  
st1=student("Anas",["Math","Physics","Chemistry"],["Computer Science"],3.5)


print(st1.name)
print(st1.subjects) 

