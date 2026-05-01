class employee:
  start_time="10am"
  end_time="4pm"
  
class teacher(employee):
  def __init__(self , subject):
    self.subject=subject 
    
  def print_tecaher_info(self):
    print(f"The teacher start time is {self.start_time} and end time is {self.end_time} and subject is {self.subject}")
    
p1= teacher("physics")
p1.print_tecaher_info()

# Multiple inheritance classes

class Teacher:
  def __init__(self,salary):
    self.salary=salary
    
class Student:
  def __init__(self , cgpa):
    self.cgpa=cgpa
  
class Assistant(Teacher , Student ):
  def __init__(self, name,salary,cgpa):
    Teacher.__init__(self, salary)
    Student.__init__(self, cgpa)
    self.name=name
    
p=Assistant("anas" , 300000, 3.85)
print(f"Assistant: {p.name}, Salary: {p.salary}, CGPA: {p.cgpa}")

  
    
    