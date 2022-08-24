# Functions

# Budget Checker
def budget_checker (question, low, high):
  error = "please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 1000, program continues 
      if 0 < response <= 1000:
        return response
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print(error)
    except ValueError:
     print(error)

# Main routine starts here

# Ask user what their budget is     
budget = budget_checker ("How much money do you have ", 0, 1000)
print("You will be spending ${}".format(budget))
print()