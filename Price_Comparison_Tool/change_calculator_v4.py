# Error Messages
budget_error = "please enter a number that is greater than 0 but less than 10000; we do not allow numbers above 10000 as we don't have change\n"

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


# Ask user what their budget is     
budget = budget_checker ("What will your budget be? ", 0, 10000)
print("You will be spending ${}".format(budget))
print()

# The amount it cost for the user's desired item
purchasing_price = 10.2

# if the budget is greater than the purchasing price, tell the user their change
if budget > purchasing_price:
  change = budget - purchasing_price
  print("Your total change willl be {}".format(change))
  print(change)

# if the purchasing_price is greater than the amount of money the user has, tell the user that they cannot afford their desired item
if purchasing_price > budget:
  print("You cannot purchase that item as the amount you are asking for exceeds the amount in your budget")