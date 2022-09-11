# Drink or chocolate function
def drink_or_chocolate(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "chocolate" or user_response  == "c":   
        user_response = "chocolate"
        return user_response

    elif user_response == "drink" or user_response  == "d":
        user_response = "drink"
        return user_response 

    else:
      print()
      print("Please enter drink or chocolate")
      print()

# Menu with prices
def menu():
  print("Here's the Menu")
  print("| Drinks (Cost Per 100ml):   |  Price: |")
  print("| Coca Cola                  |  $0.27  |")
  print("| Sprite                     |  $0.11  |")
  print("| Pepsi                      |  $0.20  |")
  print("| Red Bull                   |  $0.80  |")
  print("| Monster                    |  $0.70  |")
  print("| V                          |  $0.60  |")
  

  print()
  print("| Chocolates (Cost Per 100g):|  Price: |")
  print("| M&Ms                       |  $2.78  |")
  print("| Cadbury                    |  $1.83  |")
  print("| Skittles                   |  $2.71  |")
  print("| Snickers                   |  $1.80  |")
  print("| Mars                       |  $3.83  |")
  print("| Kit Kat                    |  $3.38  |")
  print()

menu()

choice = drink_or_chocolate("Would you like a drink or a chocolate\n")
print("You will be purchasing a {}".format(choice))

if choice == "drink":
  drink_choice = input("Please enter the drink you would like to purchase: ")
    
  if drink_choice == "coca cola":
    print("A {} beverage will cost $0.27 per 100ml".format(drink_choice))
  
  if drink_choice == "sprite":
    print("A {} beverage will cost $0.11 per 100ml".format(drink_choice)) 
  
  if drink_choice == "pepsi":
    print("A {} beverage will cost $0.20 per 100ml".format(drink_choice))
  
  if drink_choice == "red bull":
    print("A {} beverage will cost $0.80 per 100ml".format(drink_choice))
  
  if drink_choice == "monster":
    print("A {} beverage will cost $0.70 per 100ml".format(drink_choice)) 
  
  if drink_choice == "v":
    print("A {} beverage will cost $0.60 per 100ml".format(drink_choice))
  
  else:
    print()
    print("Please enter a chocolate that is on the menu")
    print()

if choice == "chocolate":
  chocolate_choice = input("Please enter the chocolate you would like to purchase: ")
    
  if chocolate_choice == "m&ms ":
    print("A {} will cost $2.78 per 100ml".format(chocolate_choice))
  
  if chocolate_choice == "cadbury":
    print("A {} will cost $1.83 per 100ml".format(chocolate_choice)) 
  
  if chocolate_choice == "skittles":
    print("A {} will cost $2.71 per 100ml".format(chocolate_choice))
  
  if chocolate_choice == "snickers":
    print("A {} beverage will cost $1.80 per 100ml".format(chocolate_choice))
  
  if chocolate_choice == "mars":
    print("A {} will cost $3.83 per 100ml".format(chocolate_choice))
  
  if chocolate_choice == "kit kat":
    print("A {} will cost $3.38 per 100ml".format(chocolate_choice)) 
  
  else:
    print()
    print("Please enter a chocolate that is on the menu")
    print()