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

menu()

choice = drink_or_chocolate("Would you like a drink or a chocolate")
print("You will be purchasing a {}".format(choice))