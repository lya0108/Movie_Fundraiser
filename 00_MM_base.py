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

# checks 
def boundary_check(question, low=None, high=None, exit_code = None, decimal = None):

    situation = ""


    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"
    
    while True:

        response = input(question).lower()
        if response == exit_code:
            return response

        elif decimal is not None:
            try:
                response = float(response)
                return response

            except ValueError:
                print("Please Enter An Number")

        else:
            try:
                response = int(response)

                # checks input is not too high or low if both upper and lower bounds are specified
                if situation == "both":
                    if response < low or response > high:
                        print("Please Enter a Number Between {} and {}".format(low, high))
                        continue

                elif situation == "low only":
                    if response < low:
                        print("Please Enter a Number That is More Than or Equal to {}".format(low))
                        continue

                return response

            # checks input is an integer
            except ValueError:
                if decimal is not None:
                    print("Please Enter a Number")
                
                else:
                    print("Please Enter an Integer (ie: A Number That Does Not Have An Decimal)")
                continue

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
    
    tickets_sold += 1

    if ask_name == "xxx":
        break

    elif ask_name != "":
        name = ask_name

    else:
        print("Name?")
    
    age = boundary_check("Hi {} Please Enter Your Age: ".format(name), 0, None, None, None)
    
    if 12 <= age:
        pass
    
    elif age < 12:
        print("Sorry Your Too Young")

tickets_total = ticket_num - tickets_sold
print("You Have Sold {} Ticket/s. You Have {} Ticket/s Remaining".format(tickets_sold, tickets_total))




