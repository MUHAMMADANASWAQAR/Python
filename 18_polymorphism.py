#overriding 
class teacher:
  def class_name(self):
    print("teacher class")
    
class student(teacher):
  def class_name(self):
    print("student class")
    
p=student()
p.class_name()

#Duck typing
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(thing):
    thing.quack()

d = Duck()
p = Person()
make_it_quack(d)
make_it_quack(p)
 