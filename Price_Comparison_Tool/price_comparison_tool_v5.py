# Error Messages
budget_error = "please enter a number that is greater than 0 but less than 10000; we do not allow numbers above 10000 as we don't have change\n"

amount_error = "please enter a number that is greater then 0 but less than or equal to 10000\n"

# Functions

# not blank
def not_blank(question):
  Valid = False

  while not Valid:   
    response = input(question)
    
    if response != "":
      return response
    else:
      print("Sorry - this can't be blank")
      print()

# Budget Checker
def budget_checker (question, low, high):
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 1000, program continues 
      if 0 < response <= 10000:
        rounded_budget = round(response, 2)
        return rounded_budget
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print(budget_error)
    except ValueError:
     print(budget_error)
      
# drink or chocolate
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

# Amount of item
def item_amount (question, low, high):
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 10000, program continues 
      if 0 <= response <= 10000:
        return response
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print(amount_error)
    except ValueError:
     print(amount_error)

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

# list of drinks and prices.  The purpose of this dictionary is to tell the program what the valid answers are.
drink_list = { "coca cola": 0.27, "sprite": 0.11, "pepsi": 0.20, "red bull": 0.80, "monster":0.70, "v": 0.60
}

chocolate_list = {
  "m&ms": 2.78, "Cadbury": 1.83,"skittles": 2.71, "snickers": 1.80, "mars": 3.83,"kit kat": 3.38
}

# Main routine starts here

# welcome the user and ask what their name is
print("Welcome to the Price Comparison Tool")
name = not_blank ("What is your amazing name: ")

print("Kia ora", name)

# Ask user what their budget is     
budget = budget_checker ("What will your budget be? ", 0, 10000)
print("You will be spending ${}".format(budget))
print()

# This variable is in charge of holding the price per 100ml/g of the user's chosen drink or chosen chocolate. The amount will change from 0 when the user has chosen their drink. If the user chooses coca cola, the price should change from 0 to 0.27 per 100ml. 
price_per_100 = 0

# Display the list of drinks
menu()

choice = drink_or_chocolate("Would you like a drink or a chocolate\n")
print("You will be purchasing a {}".format(choice))

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

paying_amount= 0

if choice == "chocolate":
  while True:
    amount = item_amount ("How many grams of {} would you like?\n".format(chocolate_choice),0,10000)
    
    
    if 0 <= amount <= 10000:
      
      paying_amount = amount/100 * price_per_100
      rounded_amount = round(amount, 2)
      rounded_paying_amount = round(paying_amount, 2)
  
      if budget >= rounded_paying_amount:
        change = budget - rounded_paying_amount
        rounded_change = round(change, 2)
        print("{}g of {} will cost ${}".format(rounded_amount, chocolate_choice, rounded_paying_amount))
        if rounded_change == 0:
          print("Thanks for coming by!")
          break
          
        else: 
          print("Your change will be ${}".format(rounded_change))
          print("Thanks for coming by!")
          break
  
      elif budget < rounded_paying_amount:
        print("You don't seem to have enough money to purchase {}g of {}".format(amount, chocolate_choice))
        maximum_amount = budget/price_per_100 *100 
        rounded_maximum_amount = round(maximum_amount, 2)
        print("The maximum amount you can purchase is {}g".format(rounded_maximum_amount))
        print()
    
    else:
      print(amount_error)
  
if choice =="drink":
  while True:
    amount = item_amount ("How many mililitres of {} would you like?\n".format(drink_choice),100,10000)
    if 0 <= amount <= 10000:
      
      paying_amount = amount/100 * price_per_100
      rounded_amount = round(amount, 2)
      rounded_paying_amount = round(paying_amount, 2)
  
      if budget >= rounded_paying_amount:
        change = budget - rounded_paying_amount
        rounded_change = round(change, 2)
        print("{}ml of {} will cost ${}".format(rounded_amount, drink_choice, rounded_paying_amount))
        if rounded_change == 0:
          print("Thanks for coming by!")
          break
          
        else: 
          print("Your change will be ${}".format(rounded_change))
          print("Thanks for coming by!")
          break
  
      elif budget < rounded_paying_amount:
        print("You don't seem to have enough money to purchase {}ml of {}".format(amount, drink_choice))
        maximum_amount = budget/price_per_100 *100
        rounded_maximum_amount = round(maximum_amount, 2)
        print("The maximum amount you can purchase is {}ml".format(rounded_maximum_amount))
        print()

    else:
      print(amount_error)