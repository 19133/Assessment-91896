while True:
  budget = float(input("Enter a budget: "))  
  # Checks if the users input is divisable by 0.20
  divisible = budget % 0.20
  print(divisible)
  if (divisible % 0.20) == 0.0:  
     print("{} is divisable by 0.20".format(budget))  
  else:  
     print("{} is not divisable by 0.20".format(budget))  