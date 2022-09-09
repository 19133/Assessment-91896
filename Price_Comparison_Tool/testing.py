# Error Messages
budget_error = "please enter a number that is greater or equal to 0.1 but less than 10000"

amount_error = "please enter a number that is greater than 0.1 but less than or equal to 10000\n"

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
      if 0.1 < response <= 10000:
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

    if user_response == "chocolate" or user_response  == "c" or user_response  == "choc":   
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
      if 0.1 < response <= 10000:
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

def recomended_item():
  # Best item = user's budget divided by $0.27
  best_item_coca_cola = budget/0.27 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was coca cola. 
  if best_item_coca_cola == 10000 or best_item_coca_cola == 1000 or best_item_coca_cola == 100 or best_item_coca_cola == 10 :
    print("The best thing to purchase was Coca Cola")

  # Best item = user's budget divided by $0.11
  best_item_sprite = budget/0.11 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was sprite. 
  if best_item_sprite == 10000 or best_item_sprite == 1000 or best_item_sprite == 100 or best_item_sprite == 10 :
    print("The best thing to purchase was Sprite")

  # Best item = user's budget divided by $0.20
  best_item_pepsi = budget/0.20 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was pepsi, red bull, v, snickers. 
  if best_item_pepsi == 10000 or best_item_pepsi == 1000 or best_item_pepsi == 100 or best_item_pepsi == 10 :
    print("The best thing to purchase was Pepsi, Red Bull, V, or Snickers")

  # Best item = user's budget divided by $0.70
  best_item_monster = budget/0.70 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was Monster 
  if best_item_monster == 10000 or best_item_monster == 1000 or best_item_monster == 100 or best_item_monster == 10 :
    print("The best thing to purchase was Monster")

  # Best item = user's budget divided by $2.78
  best_item_m_and_ms = budget/2.78 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was m&ms 
  if best_item_m_and_ms == 10000 or best_item_m_and_ms == 1000 or best_item_m_and_ms == 100 or best_item_m_and_ms == 10 :
    print("The best thing to purchase was m&ms")

  # Best item = user's budget divided by $1.83
  best_item_cadbury = budget/1.83 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was cadbury 
  if best_item_cadbury == 10000 or best_item_cadbury == 1000 or best_item_cadbury == 100 or best_item_cadbury == 10 :
    print("The best thing to purchase was cadbury")

  # Best item = user's budget divided by $2.71
  best_item_skittles = budget/2.71 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was skittles
  if best_item_skittles == 10000 or best_item_skittles == 1000 or best_item_skittles == 100 or best_item_skittles == 10 :
    print("The best thing to purchase was skittles")

  # Best item = user's budget divided by $3.83
  best_item_mars = budget/3.83 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was mars
  if best_item_mars == 10000 or best_item_mars == 1000 or best_item_mars == 100 or best_item_mars == 10 :
    print("The best thing to purchase was mars")

  # Best item = user's budget divided by $3.38
  best_item_kit_kat = budget/3.38 
  # when the budget has been divided, if the answer is 10000, 1000, 100, or 10, tell the user the best item to purchase was kit kat
  if best_item_kit_kat == 10000 or best_item_kit_kat == 1000 or best_item_kit_kat == 100 or best_item_kit_kat == 10 :
    print("The best thing to purchase was kit kat")

# list of drinks and prices.  The purpose of this dictionary is to tell the program what the valid answers are.
drink_list = { "coca cola" : 0.27, "sprite" : 0.11, "pepsi" : 0.20, "red bull" : 0.80, "monster" :0.70, "v" : 0.60
}

# list of chocolates and prices.  The purpose of this dictionary is to tell the program what the valid answers are.
chocolate_list = {
  "m&ms" : 2.78, "cadbury" : 1.83,"skittles" : 2.71, "snickers" : 1.80, "mars" : 3.83,"kit kat" : 3.38
}

# Main routine starts here

# welcome the user and ask what their name is
print("Welcome to the Price Comparison Tool")
name = not_blank ("What is your amazing name: ")

print("Kia ora", name)

# Ask user what their budget is     
budget = budget_checker ("What will your budget be? ", 0.1, 10000)
print("You will be spending ${}".format(budget))
print()

# This variable is in charge of holding the price per 100ml/g of the user's chosen drink or chosen chocolate. The amount will change from 0 when the user has chosen their drink. e.g. If the user chooses coca cola, the price should change from 0 to 0.27 per 100ml. 
price_per_100 = 0

# Display the list of drinks
menu()

# Ask user whether they want a drink or a chocolate
choice = drink_or_chocolate("Would you like a drink or a chocolate\n")
# Tell their choice (Chocolate or drink)
print("You will be purchasing a {}".format(choice))

# Program will execute the lines of code below if user chose drink over chocolate
if choice == "drink":
  # loop the code until a break is met
  while True:
    # asks user what drink they would like
    drink_choice = input("Please enter the drink you would like to purchase: " ).lower()

    # if the user's chosen drink is in the drink_list dictionary above, tell the user their chosen drink
    if drink_choice.lower() in drink_list:
      print("You will be purchasing {}".format(drink_choice)) 

      # the price for per 100ml of the drink will equal the amount it cost for the drink
      price_per_100 = drink_list[drink_choice]

      # tell the user the name of their chosen drink and how much it cost per 100ml
      print("A {} beverage will cost ${} per 100ml".format(drink_choice, price_per_100)) 
      # end the loop
      break

    # if the user inputs a value that is not on the drink menu/not in the drink_list dictionary, ask the user to enter a drink that is on the menu and continue the loop
    else:
      print("Please enter a {} that is on the menu".format(choice))
      print()

# Program will execute the lines of code below if the user chose chocolate over drink
if choice == "chocolate":
  # loop the code until a break is met
  while True:
    # asks user what chocolate they would like
    chocolate_choice = input("Please enter the chocolate you would like to purchase: " ).lower()

    # If the user's chosen chocolate is in the chocolate_list dictionary above, tell the user their chosen chocolate
    if chocolate_choice.lower() in chocolate_list:
      print("You will be purchasing {}".format(chocolate_choice)) 

      # the price for per 100g of the chocolate will equal the amount it cost for the chocolate. So if the user chose kit kat, the price_per_100 will equal $3.38
      price_per_100 = chocolate_list[chocolate_choice]

      # Tell the user the name of their chosen chocolate and how much it cost
      print("A {} will cost ${} per 100g".format(chocolate_choice, price_per_100)) 
      # end the loop
      break
    # if the user inputs a value that is not on the chocolate menu/not in the chocolate_list dictionary, ask the user to enter a drink that is on the menu and continue the loop
    else:
      print("Please enter a {} that is on the menu".format(choice))
      print()

# execute the lines of code below if the user chose a drink.
if choice =="drink":
  # loop the code until a break is met
  while True:
    # ask the user how many mililitres of their drink they would like
    amount = item_amount ("How many mililitres of {} would you like?\n".format(drink_choice),0.1,10000)
    # if the amount the user is asking for is greater than 0 but less than 10000, program continues
    if 0.1 < amount <= 10000:

      # calculate the cost of the user's desired amount. So if the user asks for 234ml of pepsi, this equation below will calculate the exact cost of 234ml of pepsi
      paying_amount = amount/100 * price_per_100
      # round the amount so when I tell the user the amount, it looks nice.
      rounded_amount = round(amount, 2)
      # round the paying amount so the are only 2 numbers after the decimal point. 
      rounded_paying_amount = round(paying_amount, 2)

      # if the budget is greater than or equal to the cost of the user's desired item, print the change.
      if budget >= rounded_paying_amount:
        # calculate the change
        change = budget - rounded_paying_amount
        # round the change
        rounded_change = round(change, 2)
        print("{}ml of {} will cost ${}".format(rounded_amount, drink_choice, rounded_paying_amount))
        # if the change == 0, don't tell the user their change. 
        if rounded_change == 0:
          # end the loop
          break

        # if change != 0 (doesn't equal 0), tell the user their change 
        else: 
          print("Your change will be ${}".format(rounded_change))
          # end the loop
          break

      # if the user's budget is less than the cost of their item, tell the user to enter a new amount and tell them the maximum amount they can purchase.
      elif budget < rounded_paying_amount:
        print("You don't seem to have enough money to purchase {}ml of {}".format(rounded_amount, drink_choice))
        # Program calculates the maximum amount the user can purchase. The -1 is there because due to rounding issues, the program might sometimes print out an amount that is 1 or 2 mililitres off the actual maximum amount. So to make sure the program isn't lying, we minused it by one.
        maximum_amount = budget/price_per_100 *100 -1
        # round maximum amount to 0dp. I did 0dp becuase 
        rounded_maximum_amount = round(maximum_amount, 0)
        print("We recomend purchasing something around {}ml as that's roughly the maximum amount you can purchase".format(rounded_maximum_amount))
        print()

    # if the user types an integer that is less than 0 or greater than 1000, print an error
    else:
      print(amount_error)

# execute the lines of code below if the user chose chocolate.
if choice == "chocolate":
  # loop the code until a break is met
  while True:
    # ask the user how many mililitres of their chocolate they would like
    amount = item_amount ("How many grams of {} would you like?\n".format(chocolate_choice),0.1,10000)
    
    # if the amount the user is asking for is greater than 0 but less than 10000, program continues
    if 0.1< amount <= 10000:

      # calculate the cost of the user's desired amount. So if the user asks for 234ml of pepsi, this equation below will calculate the exact cost of 234ml of pepsi
      paying_amount = amount/100 * price_per_100
      # round the amount so when I tell the user the amount, it looks nice.
      rounded_amount = round(amount, 2)
      # round the paying amount so the are only 2 numbers after the decimal point. 
      rounded_paying_amount = round(paying_amount, 2)

      # if the budget is greater than or equal to the cost of the user's desired item, print the change.
      if budget >= rounded_paying_amount:
        # calculate the change
        change = budget - rounded_paying_amount
        # round the change
        rounded_change = round(change, 2)
        print("{}g of {} will cost ${}".format(rounded_amount, chocolate_choice, rounded_paying_amount))
        # if the change == 0, don't tell the user their change.
        if rounded_change == 0:
          # end the loop
          break

        # if change != 0 (doesn't equal 0), tell the user their change   
        else: 
          print("Your change will be ${}".format(rounded_change))
          # end the loop
          break
  
      elif budget < rounded_paying_amount:
        print("You don't seem to have enough money to purchase {}g of {}".format(rounded_amount, chocolate_choice))
        # Program calculates the maximum amount the user can purchase. The -1 is there because due to rounding issues, the program might sometimes print out an amount that is 1 or 2 grams off the actual maximum amount. So to make sure the program isn't lying, we minused it by one.
        maximum_amount = budget/price_per_100 *100 -1
        # round maximum amount to 0dp. I did 0dp becuase 
        rounded_maximum_amount = round(maximum_amount, 0)
        print("We recomend purchasing something around {}g as thats roughly the maximum amount you can purchase".format(rounded_maximum_amount))
        print()

    # if the user types an integer that is less than 0 or greater than 1000, print an error
    else:
      print(amount_error)

recomended_item()

print("Thanks for coming by!")