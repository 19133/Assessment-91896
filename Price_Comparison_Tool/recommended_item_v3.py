while True:
  budget = float(input("Enter a budget: "))  
  # Checks if the users input is divisable by 0.20
  divisible = budget % 0.20
  rounded_divisible = round(divisible, 2)
  print(rounded_divisible)
  if (rounded_divisible % 0.20) == 0.0:  
    print("{} is divisable by 0.20".format(budget))  
  else:  
     print("{} is not divisable by 0.20".format(budget))  