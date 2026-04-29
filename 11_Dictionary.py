information ={
  "name": "Muhammad",
  "age":25,
   "info": {
     "city":"Karachi",
     "country":"Pakistan"
   }
  
}
print(information["info"]["city"])

class anas :
  information ={
  "name": "Muhammad",
  "age":25,
   "info": {
     "city":"Karachi",
     "country":"Pakistan"
   }
  
}
anas.information["info"]["city"] = "Lahore"
print(anas.information)



# MEthods in dictionary
# 1. keys() method  
print(anas.information.keys())
#2. values() method
print(anas.information.values())
# 3. items() method
print(anas.information.items())
# 4. get() method
print(anas.information.get("name"))
# 5. update() method
anas.information.update({"practics": 26})
print(anas.information)
