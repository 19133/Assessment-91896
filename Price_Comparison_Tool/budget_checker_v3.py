# Functions

# Budget Checker
def budget_checker (question, low, high):
  error = "please enter a whole number between 1 and 10000"
  valid = False
  while not valid:
    try:
      response = float(input(question))
      # If the user types a whole number between 1 and 10000, program continues 
      if 1 < response <= 10000:
        global rounded_response
        rounded_response =round(response, 2)
        return rounded_response
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
budget = budget_checker ("What is your budget? ", 1, 10000)
print("You will be spending ${}".format(budget))
print()