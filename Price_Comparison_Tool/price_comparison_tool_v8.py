# Error Messages
budget_error = "Please enter a number that is greater than or equal to 0.1 but less than or equal to 10000"

# Amount Error
amount_error = "Please enter a number that is greater than 1 but less than or equal to 10000\n"

# Functions

# not blank
def not_blank(question):
  Valid = False

  while not Valid:   
    response = input(question)

    # if name doesn't equal blank, program continues
    if response != "":
      return response
    # if name equals blank, print an error
    else:
      print()
      print("Sorry - this can't be blank")
      print()

# Budget Checker
def budget_checker (question, low, high):
  valid = False
  while not valid:
    # program checks for errors except for ValueError
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 1000, program continues 
      if 0.1 <= response <= 10000:
        # Globalising the rounded_budget so it can be used anywhere.
        global rounded_budget 
        # Rounding the budget to 2dp just in case
        rounded_budget = round(response, 2)
        return rounded_budget
      else:
        # If the user types an invalid number, print an error and reask the question
        print()
        print(budget_error)
        print()
    except ValueError:
     print()
     print(budget_error)
     print()
      
# drink or chocolate
def drink_or_chocolate(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    # if response is chocolate, the user will be purchasing a chocolate
    if user_response == "chocolate" or user_response  == "c" or user_response  == "choc":   
        user_response = "chocolate"
        return user_response

    # if response is chocolate, the user will be purchasing a chocolate
    elif user_response == "drink" or user_response  == "d":
        user_response = "drink"
        return user_response 

    # else
    else:
      print()
      print("Please enter drink or chocolate") 
      print()

# Amount of item
def item_amount (question, low, high):
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 10000, program continues 
      if 1 <= response <= 10000:
        return response
      else:
        # If the user types an invalid number, print an error and re-ask the main question
        print()
        print(amount_error)
        print()
    except ValueError:
     print()
     print(amount_error)
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

def recommended_item():

  # Recommend Coca Cola = budget / 0.27
  recommend_coca_cola = budget % 0.27
  # Round the answer of budget % 0.27.
  rounded_recommend_coca_cola = round(recommend_coca_cola, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was Coca Cola
  if (rounded_recommend_coca_cola % 0.27) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was Coca Cola ".format(budget)) 


  # Recommend Sprite = budget / 0.11
  recommend_sprite = budget % 0.11
  # Round the answer of budget % 0.11.
  rounded_recommend_sprite = round(recommend_sprite, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was sprite
  if (rounded_recommend_sprite % 0.11) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was Sprite ".format(budget))   

  # Recommend pepsi = budget / 0.20
  recommend_pepsi = budget % 0.20
  # Round the answer of budget % 0.20.
  rounded_recommend_pepsi = round(recommend_pepsi, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was pepsi
  if (rounded_recommend_pepsi % 0.20) == 0.0:  
    # Red Bull, V, and Snickers are also recommended items because the prices for those items are divisable by 0.20 as well. (redbull is 0.80, v is 0.70, snickers is 1.80)
     print("With your budget of ${}, the best thing to purchase was Pepsi, Red Bull, V, or Snickers".format(budget))   


  # Recommend monster = budget / 0.70
  recommend_monster = budget % 0.70
  # Round the answer of budget % 0.70.
  rounded_recommend_monster = round(recommend_monster, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was monster
  if (rounded_recommend_monster % 0.70) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was Monster".format(budget))  

  # Recommend m&ms = budget / 2.78
  recommend_m_and_ms = budget % 2.78
  # Round the answer of budget % 2.78
  rounded_recommend_m_and_ms = round(recommend_m_and_ms, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was M&Ms
  if (rounded_recommend_m_and_ms % 2.78) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was M&Ms".format(budget))  

  # Recommend cadbury = budget / 1.83
  recommend_cadbury = budget % 1.83
  # Round the answer of budget % 1.83
  rounded_recommend_cadbury = round(recommend_cadbury, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was cadbury
  if (rounded_recommend_cadbury % 1.83) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was Cadbury".format(budget))   

  # Recommend skittles = budget / 2.71
  recommend_skittles = budget % 2.71
  # Round the answer of budget % 2.71
  rounded_recommend_skittles = round(recommend_skittles, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was skittles
  if (rounded_recommend_skittles % 2.71) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was Skittles".format(budget)) 

  # Recommend Mars = budget / 3.83
  recommend_mars = budget % 3.83
  # Round the answer of budget % 3.83
  rounded_recommend_mars = round(recommend_mars, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was Mars
  if (rounded_recommend_mars % 3.83) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was Mars".format(budget)) 

  # Recommend Kit Kat = budget / 3.38
  recommend_kit_kat = budget % 3.38
  # Round the answer of budget % 3.38
  rounded_recommend_kit_kat = round(recommend_kit_kat, 2)
  # When the budget has been divided, if the remainder is 0, tell the user the best thing to purchase was Kit Kat
  if (rounded_recommend_kit_kat % 3.38) == 0.0:  
     print("With your budget of ${}, the best thing to purchase was Kit Kat".format(budget)) 

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
      print()
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
      print()
      print("Please enter a {} that is on the menu".format(choice))
      print()

# execute the lines of code below if the user chose a drink.
if choice =="drink":
  # loop the code until a break is met
  while True:
    # ask the user how many mililitres of their drink they would like
    amount = item_amount ("How many mililitres of {} would you like? You could purchase 10000ml of {} if you have the money; or even 1ml\n".format(drink_choice, drink_choice),1 ,10000)
    # if the amount the user is asking for is greater than 0 but less than 10000, program continues
    if 1 < amount <= 10000:

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
        print()
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
        print()
        print("You don't seem to have enough money to purchase {}ml of {}".format(rounded_amount, drink_choice))
        # Program calculates the maximum amount the user can purchase
        maximum_amount = budget/price_per_100 *100
        # round maximum amount to 2dp.
        rounded_maximum_amount = round(maximum_amount, 2)
        print("We recommend purchasing {}ml as that's the maximum amount you can purchase with your budget of ${}".format(rounded_maximum_amount, rounded_budget))
        print()

    # if the user types an integer that is less than 0 or greater than 1000, print an error
    else:
      print()
      print(amount_error)
      print()

# execute the lines of code below if the user chose chocolate.
if choice == "chocolate":
  # loop the code until a break is met
  while True:
    # ask the user how many mililitres of their chocolate they would like
    amount = item_amount ("How many grams of {} would you like? You could purchase 10000g of {} if you have the money; or even 1g\n".format(chocolate_choice, chocolate_choice),1,10000)
    
    # if the amount the user is asking for is greater than 0 but less than 10000, program continues
    if 1< amount <= 10000:

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
        print()
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
        print()
        print("You don't seem to have enough money to purchase {}g of {}".format(rounded_amount, chocolate_choice))
        # Program calculates the maximum amount the user can purchase
        maximum_amount = budget/price_per_100 *100 
        # round maximum amount to 2dp.
        rounded_maximum_amount = round(maximum_amount, 2)
        print("We recommend purchasing {}g as thats the maximum amount you can purchase with your budget of ${}".format(rounded_maximum_amount, rounded_budget))
        print()

    # if the user types an integer that is less than 0 or greater than 1000, print an error
    else:
      print()
      print(amount_error)
      print()

# Tell the user their recommmended item (that is if there is one)
print()
recommended_item()

print()
print("Thanks for coming by!")