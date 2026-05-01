from abc import ABC , abstractmethod
class animal (ABC):
  def make_sound(self):
    pass

class lion(animal):
  def make_sound(self):
    print("Roar")
    
class cow (animal):
  def make_sound(self):
   print("Moo")
p=lion()
p.make_sound()
p1=cow()
p1.make_sound()