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
drink_list = { "coca cola": 0.27, "sprite": 0.11, "pepsi": 0.20, "red bull": 0.80, "monster":0.70, "v": 0.60
}

chocolate_list = {
  "m&ms": 2.78, "Cadbury": 1.83,"skittles": 2.71, "snickers": 1.80, "mars": 3.83,"kit kat": 3.38
}

# main routine starts here

choice = drink_or_chocolate("Would you like a drink or a chocolate")
print("You will be purchasing a {}".format(choice))

if choice == "chocolate":
  while True:
    # asks user what drink they would like
    chocolate_choice = input("Please enter the chocolate you would like to purchase: " )
    
    if chocolate_choice.lower() in chocolate_list:
      print("You will be purchasing {}".format(chocolate_choice)) 

      price_per_100 = chocolate_list[chocolate_choice]
      
      print("A {} will cost ${} per 100g".format(chocolate_choice, price_per_100)) 
      break
    else:
      print("Please enter a {} that is on the menu".format(choice))
      print()

if choice == "drink":
  while True:
    # asks user what drink they would like
    drink_choice = input("Please enter the drink you would like to purchase: " )
  
    if drink_choice.lower() in drink_list:
      print("You will be purchasing {}".format(drink_choice)) 
  
      price_per_100 = drink_list[drink_choice]

      print("A {} beverage will cost ${} per 100ml".format(drink_choice, price_per_100)) 
      break
    else:
      print("Please enter a {} that is on the menu".format(choice))
      print()