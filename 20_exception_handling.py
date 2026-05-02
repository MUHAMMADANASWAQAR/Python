try:
    x = int(input("Enter a number: "))
    ans = 10 / x
except ZeroDivisionError:
    print("We cannot divide by zero.")
except ValueError:
    print("Invalid number.")
else:
    print(f"ans: {ans}")
finally:
    print("End of the programme")
  
    