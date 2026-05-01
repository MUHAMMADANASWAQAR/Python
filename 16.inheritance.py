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