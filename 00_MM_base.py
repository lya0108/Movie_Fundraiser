# functions

# checks that choice is within choosen list
def choice_checker(question, valid_list, error):

    valid = False
    while not valid:
        
        # asks user for choice
        response = input(question).lower()

        # checks if input is in list
        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        print(error)
        print()

# lists
maybe = ["yes", "no"]

# set constants
tickets_sold = 0
ticket_num = 3

# ask if instructions display
intro = choice_checker("Do You Want To Read Instructions: ", maybe, "Please Enter Yes or No")

if intro == "yes":
    print("Blab Blah Bloh")
    
while tickets_sold < ticket_num:
    ask_name = input("Please Enter Your Name or 'xxx' to quit: ")
  
    if ask_name == "xxx":
        break

    elif ask_name != "":
        name = ask_name

    else:
        print("Name?")




