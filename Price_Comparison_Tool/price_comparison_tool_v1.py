# Functions

# Not blank function
def not_blank(question):
  Valid = False

  while not Valid:   
    response = input(question)

    # If the user doesn't type something that isn't blank, return response
    if response != "":
      return response
    # Else, tell the user that they're name can't be blank and ask the question again. 
    else:
      print("Sorry - this can't be blank")

# Budget Checker Function
def budget_checker (question, low, high):
  error = "please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"
  valid = False
  while not valid:
    try:
      response = int(input(question))
      # If the user types a whole number between 1 and 1000, program continues 
      if 0 < response <= 1000:
        return response
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print(error)
    except ValueError:
     print(error)
      
# Main routine starts here

# List of items

      
# Welcome the user to the price comparison tool
print("Welcome to the Price Comparison Tool")
# Ask user what their name is
name = not_blank ("What is your amazing name: ")

# Greet the user
print("Kia ora", name)

# Ask user what their budget is     
budget = budget_checker ("How much money do you have ", 0, 1000)
print("You will be spending ${}".format(budget))
print()

# Show user a list of items and ask the user what item they would like

# Recommend what item the user should buy depending on how much money they have. 

# Ask user how much they would like their desired item to weigh

# Ask user how much they would like their desired item to weigh (if they choose a drink, ask how many litres they would like)

# Ask the user how much sugar they would like to have in their item. If they choose a drink, ask how much cafine they would like their item to have. If they say yes, add extra money to the total cost 

# Tell the user how much money it would cost to purchase that item with their desired increments

# Recommend what item the user should buy depending on how much money they have