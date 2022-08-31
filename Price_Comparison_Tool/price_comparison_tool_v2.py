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

# Budget Checker
def budget_checker (question, low, high):
  error = "please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"
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
     print(error)
      
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
  error = "please enter a whole number that is greater then 100 but less than or equal to 10000\n"
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 1000, program continues 
      if 0 < response <= 10000:
        return response
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print(error)
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
  print("| Chocolates (Cost Per 100g):|  Price  |")
  print("| M&Ms                       |  $2.78  |")
  print("| Cadbury                    |  $1.83  |")
  print("| Skittles                   |  $2.71  |")
  print("| Hersheys                   |  $3.39  |")
  print("| Mars                       |  $3.83  |")
  print("| Kit Kat                    |  $3.38  |")
  print()

# list of drinks and prices.  The purpose of this dictionary is to tell the program what the valid answers are.
drink_list = { "coca cola", "sprite", "pepsi", "red bull", "monster", "v"
}

chocolate_list={
  "m&ms", "Cadbury","skittles", "hersheys", "mars","kit kat"
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

# This variable is in charge of holding the price per 100ml of the user's chosen drink. The amount will change from 0 when the user has chosen their drink. If the user chooses coca cola, the price should change from 0 to 0.27 per 100ml. 
price_per_100ml/g = 0

# Display the list of drinks
menu()

print

choice = drink_or_chocolate("Would you like a drink or a chocolate\n")
print("You will be purchasing a {}".format(choice))

if choice == "drink":
  while True:
    # asks user what drink they would like
    drink_choice = input("Please enter the drink you would like to purchase: " )
  
    if drink_choice.lower() in drink_list:
      print("You will be purchasing {}".format(drink_choice)) 
  
      # if the user chooses coca cola, the price per 100ml will be 0.27
      if drink_choice.lower() == "coca cola":
        price_per_100ml/g = 0.27
      # if the user chooses sprite, the price per 100ml will be 0.11
      elif drink_choice.lower() == "sprite":
        price_per_100ml/g = 0.11
      # if the user chooses pepsi, the price per 100ml will be 0.20
      elif drink_choice.lower() == "pepsi":
        price_per_100ml/g = 0.20
      # if the user chooses red bull, the price per 100ml will be 0.80
      elif drink_choice.lower() == "red bull":
        price_per_100ml/g = 0.80
      # if the user chooses monster, the price per 100ml will be 0.70
      elif drink_choice.lower() == "monster":
        price_per_100ml/g = 0.70
      # if the user chooses v, the price per 100ml will be 0.60
      elif drink_choice.lower() == "v":
        price_per_100ml/g = 0.60
      print("A {} beverage will cost ${} per 100ml".format(drink_choice, price_per_100ml/g)) 
      break

if choice == "chocolate":
  while True:
    # asks user what drink they would like
    chocolate_choice = input("Please enter the chocolate you would like to purchase: " )
  
    if chocolate_choice.lower() in chocolate_list:
      print("You will be purchasing {}".format(chocolate_choice)) 
  
      # if the user chooses coca cola, the price per 100ml will be 0.27
      if chocolate_choice.lower() == "coca cola":
        price_per_100ml/g = 0.27
      # if the user chooses sprite, the price per 100ml will be 0.11
      elif chocolate_choice.lower() == "sprite":
        price_per_100ml/g = 0.11
      # if the user chooses pepsi, the price per 100ml will be 0.20
      elif chocolate_choice.lower() == "pepsi":
        price_per_100ml/g = 0.20
      # if the user chooses red bull, the price per 100ml will be 0.80
      elif chocolate_choice.lower() == "red bull":
        price_per_100ml/g = 0.80
      # if the user chooses monster, the price per 100ml will be 0.70
      elif chocolate_choice.lower() == "monster":
        price_per_100ml/g = 0.70
      # if the user chooses v, the price per 100ml will be 0.60
      elif chocolate_choice.lower() == "v":
        price_per_100ml/g = 0.60
      print("A {} beverage will cost ${} per 100ml".format(chocolate_choice, price_per_100ml/g)) 
      break

paying_amount= 0

if choice == "chocolate":
  amount= float("How many grams of {} would you like (the maximum amount is 1000g".format(chocolate_choice),100,1000)
  
  

if choice =="drink":
  while True:
    amount = item_amount ("How many mililitres of {} would you like(the maximum amount is 1000ml\n".format(drink_choice),100,10000)
    if 100 < amount <= 10000:
      
      paying_amount = amount/100 * price_per_100ml/g
      rounded_paying_amount = round(paying_amount, 2)
  
      if budget > rounded_paying_amount:
        change = budget - rounded_paying_amount
        rounded_change = round(change, 2)
        print("{}ml of {} will cost ${}".format(amount, drink_choice, rounded_paying_amount))
        print("Your change will be ${}".format(rounded_change))
        break
  
      elif budget < rounded_paying_amount:
        print("You don't seem to have enough money to purchase {}ml of {}".format(price_per_100ml/g, drink_choice))
        maximum_amount = paying_amount * budget
        print("The maximum amount you can purchase is {}ml".format(maximum_amount))

    else:
      print(error)

# Ask Mr what his price comparison tool works 
    
      
      



        # divide the amount by 100 then multiply it with the price per 100ml. So if the user says they want 300ml of pepsi($0.20 per 100ml), divide the 300 by 100 (so 3) and then multiply it with the price per 100ml(0.20). So 300 divide 100 times 0.20 which would equal $0.60. 