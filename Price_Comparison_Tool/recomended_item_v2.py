while True:
  num = float(input("Enter a number: "))  
  # Checks if the users input is divisable by 0.20
  divisible = num % 0.20
  rounded_divisible = round(divisible, 2)
  if (rounded_divisible % 0.20) == 0.0:  
     print("{} is divisable by 0.20".format(num))  
  else:  
     print("{} is not divisable by 0.20".format(num))  