# Functions

budget_error = "please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"

amount_error = "please enter a whole number that is greater then 100 but less than or equal to 10000\n"

# not blank
def not_blank(question):
  Valid = False

  while not Valid:   
    response = input(question)
    
    if response != "":
      return response
    else:
      print("Sorry - this can't be blank")

# Budget Checker
budget_error = "please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"
def budget_checker (question, low, high):
  budget_error = "please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 1000, program continues 
      if 0 < response <= 1000:
        rounded_budget = round(response, 2)
        return rounded_budget
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print(error)
    except ValueError:
     print(budget_error)
      
# drink or chocolate
amount_error = "please enter a whole number that is greater then 100 but less than or equal to 10000\n"
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
  amount_error = "please enter a whole number that is greater then 100 but less than or equal to 10000\n"
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 10000, program continues 
      if 0 < response <= 10000:
        return response
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print(amount_error)
    except ValueError:
     print(error)


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
drink_list = { "coca cola", "sprite", "pepsi", "red bull", "monster", "v"
}

chocolate_list = {
  "m&ms", "Cadbury","skittles", "snickers", "mars","kit kat"
}

# Main routine starts here

# welcome the user and ask what their name is
print("Welcome to the Price Comparison Tool")
name = not_blank ("What is your amazing name: ")

print("Kia ora", name)

# Ask user what their budget is     
budget = budget_checker ("How much money do you have ", 0, 1000)
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

paying_amount= 0

if choice == "chocolate":
  while True:
    amount = item_amount ("How many grams of {} would you like (the maximum amount is 1000g\n".format(chocolate_choice),100,10000)
    
    
    if 100 < amount <= 10000:
      
      paying_amount = amount/100 * price_per_100
      rounded_paying_amount = round(paying_amount, 2)
  
      if budget > rounded_paying_amount:
        change = budget - rounded_paying_amount
        rounded_change = round(change, 2)
        print("{}g of {} will cost ${}".format(amount, chocolate_choice, rounded_paying_amount))
        print("Your change will be ${}".format(rounded_change))
        break
  
      elif budget < rounded_paying_amount:
        print("You don't seem to have enough money to purchase {}ml of {}".format(price_per_100, chocolate_choice))
        maximum_amount = budget/price_per_100 *price_per_100
        print("The maximum amount you can purchase is {}ml".format(maximum_amount))
    
    else:
      print(amount_error)
  
if choice =="drink":
  while True:
    amount = item_amount ("How many mililitres of {} would you like(the maximum amount is 1000ml\n".format(drink_choice),100,10000)
    if 100 < amount <= 10000:
      
      paying_amount = amount/100 * price_per_100
      rounded_paying_amount = round(paying_amount, 2)
  
      if budget > rounded_paying_amount:
        change = budget - rounded_paying_amount
        rounded_change = round(change, 2)
        print("{}ml of {} will cost ${}".format(amount, drink_choice, rounded_paying_amount))
        print("Your change will be ${}".format(rounded_change))
        break
  
      elif budget < rounded_paying_amount:
        print("You don't seem to have enough money to purchase {}ml of {}".format(price_per_100, drink_choice))
        maximum_amount = budget/price_per_100 *price_per_100
        print("The maximum amount you can purchase is {}ml".format(maximum_amount))

    else:
      print(amount_error)