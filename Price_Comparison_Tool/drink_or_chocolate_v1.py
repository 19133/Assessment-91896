# Functions

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
      print()
      print("Please enter drink or chocolate")
      print()

# Main routine goes here

choice = drink_or_chocolate("Would you like a drink or a chocolate")
print("You will be purchasing a {}".format(choice))
