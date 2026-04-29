color= str(input("Enter a color : ")  )
match color:
  case "red":
      print("The color is red")
  case "blue":
      print("The color is blue")
  case _:
      print("The Select color is neither blue nor red ")    
      