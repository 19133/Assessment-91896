# Functions

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

# list of drinks and prices.  The purpose of this dictionary is to tell the program what the valid answers are.
drink_list = { "coca cola", "sprite", "pepsi", "red bull", "monster", "v"
}

chocolate_list = {
  "m&ms", "Cadbury","skittles", "snickers", "mars","kit kat"
}

# Main routine starts here

choice = drink_or_chocolate("Would you like a drink or a chocolate")
print("You will be purchasing a {}".format(choice))

if choice == "drink":
  while True:
    # asks user what drink they would like
    drink_choice = input("Please enter the drink you would like to purchase: ")
  
    if drink_choice.lower() in drink_list:
      print("You will be purchasing {}".format(drink_choice)) 
  
      # if the user chooses coca cola, the price per 100ml will be 0.27
      if drink_choice.lower() == "coca cola" :
        price_per_100 = 0.27
      # if the user chooses sprite, the price per 100ml will be 0.11
      elif drink_choice.lower() == "sprite": 
        price_per_100 = 0.11
      # if the user chooses pepsi, the price per 100ml will be 0.20
      elif drink_choice.lower() == "pepsi":
        price_per_100 = 0.20
      # if the user chooses red bull, the price per 100ml will be 0.80
      elif drink_choice.lower() == "red bull":
        price_per_100 = 0.80
      # if the user chooses monster, the price per 100ml will be 0.70
      elif drink_choice.lower() == "monster":
        price_per_100 = 0.70
      # if the user chooses v, the price per 100ml will be 0.60
      elif drink_choice.lower() == "v":
        price_per_100 = 0.60
      print("A {} beverage will cost ${} per 100ml".format(drink_choice, price_per_100)) 
      break
    else:
      print("Please enter a {} that is on the menu".format(choice))
      print()
    
if choice == "chocolate":
  while True:
    # asks user what drink they would like
    chocolate_choice = input("Please enter the chocolate you would like to purchase: " )
    
    if chocolate_choice.lower() in chocolate_list:
      print("You will be purchasing {}".format(chocolate_choice)) 
  
      # if the user chooses snickers, the price per 100g will be $1.80
      if chocolate_choice.lower() == "snickers":
        price_per_100 = 1.80
      # if the user chooses cadbury, the price per 100g will be $1.83
      elif chocolate_choice.lower() == "cadbury":
        price_per_100 = 1.83
      # if the user chooses skittles, the price per 100g will be $2.71
      elif chocolate_choice.lower() == "skittles":
        price_per_100 = 2.71
      # if the user chooses M&Ms, the price per 100g will be $2.78
      elif chocolate_choice.lower() == "m&ms":
        price_per_100 = 2.78
      elif chocolate_choice.lower() == "kit kat":
        price_per_100 = 3.38
      elif chocolate_choice.lower() == "mars":
        price_per_100 = 3.83
      print("A {} will cost ${} per 100g".format(chocolate_choice, price_per_100)) 
      break
    else:
      print("Please enter a {} that is on the menu".format(choice))
      print()