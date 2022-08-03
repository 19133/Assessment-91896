# Functions go here

def not_blank(question):
  Valid = False

  while not Valid:   
    response = input(question)
    
    if response != "":
      return response
    else:
      print("Sorry - this can't be blank")

# Main routine starts here

print("Welcome to the Price Comparison Tool")

# Ask user what their name is
name = not_blank ("What is your amazing name: ")

print("Kia ora", name)

# Ask user what their budget is
print("What is your budget", name)
budget = input()
print("Thanks for letting us know that you have", budget)