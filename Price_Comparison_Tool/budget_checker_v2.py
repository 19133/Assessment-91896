# Functions

# Budget Checker
def budget_checker (question, low, high):
  error = "please enter a number between 1 and 10000"
  valid = False
  while not valid:
    try:
      response = int(input(question))
      # If the user types a whole number between 1 and 1000, program continues 
      if 0 < response <= 1000:
        return response
      else:
        # If the user types a number with a decimal or a number that is written in letters, print an error
        print()
        print(error)
        print()
    except ValueError:
     print()
     print(error)
     print()
# Main routine starts here

# Ask user what their budget is     
budget = budget_checker ("What is your budget ", 0, 10000)
print("You will be spending ${}".format(budget))
print()