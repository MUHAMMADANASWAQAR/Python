class Bank:
  def __init__(self):
    self.__balance=100

  def get_balance(self):
    return self.__balance
  def setter(self,price):
    self.__balance=price
  
p1=Bank()
print(p1.get_balance())
p1.setter(102)
print(p1.get_balance())
