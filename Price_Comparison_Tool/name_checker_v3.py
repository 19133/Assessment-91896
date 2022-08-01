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
name = not_blank ("What is your amazing name: ")

print("Kia ora", name)