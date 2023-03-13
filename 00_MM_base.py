import pandas as pd
import random as rd
from datetime import date

# functions

# checks input is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("This can't be blank.")

# rounds a number to 2 decimal places
def currency(x):
    
    return "${:.2f}".format(x)

# checks that choice is within choosen list
def choice_checker(question, valid_list, error, num_letters):

    while True:
        
        # asks user for choice
        response = input(question).lower()

        # checks if input is in list
        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item
        
        print(error)
        print()

# checks input is a number, if it is within set boundaries, if the input is the exit string, and if the number is a decimal.
def num_check(question, low=None, high=None, exit_code = None, decimal = None):

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
                print("Please Enter A Number")

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

# calculates ticket cost based on age
def ticket_price(yrs_old):
    global ticket_cost

    if yrs_old < 12:
        ticket_cost = 0

    elif 12 <= yrs_old < 16:
        ticket_cost = 7.50

    elif 16 <= yrs_old < 65:
        ticket_cost = 10.50

    elif 65 <= yrs_old <= 120 :
        ticket_cost = 6.50
    
    else:
        ticket_cost = 0

    return ticket_cost

# Instructions
def instructions():
    print("\nFor Each Ticket\nEnter The Person's Name\nThen Enter Their Age\nThen Enter A Payment Method")

# lists
maybe = ["yes", "no"]
cash_credit = ["cash", "credit"]

all_names = []
all_ages = []
all_ticket_costs = []
surcharge_list = []

# dictionary
mini_movie_dict = {
    "Name": all_names,
    "Age": all_ages,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge_list
}

# set constants
tickets_sold = 0
tickets_total = 50

# ask if instructions display, if yes show instructions
intro = choice_checker("Do You Want To Read Instructions: ", maybe, "Please Enter Yes or No", 1)
if intro == "yes":
    instructions()
print()

# start of loop    
while tickets_sold < tickets_total:
    
    # asks for users name
    ask_name = not_blank("Please Enter Your Name or 'xxx' to quit: ")

    # exit code
    if ask_name == "xxx" and len(all_names) > 0:
        break
    elif ask_name =="xxx":
        print("You Need To Sell At Least 1 Ticket Before Quitting")
    
    # asks user for age
    age = num_check(f"Hi {ask_name} Please Enter Your Age: ", 0, None, None, None)
    
    if 12 <= age <= 120:
        tickets_sold += 1
        pass
    
    elif age < 12:
        print("Sorry Your Too Young")

    else:
        print("HAHAHAHAHA SO FUNNY")
    
    # calculate price of ticket, if too young no ticket
    ticket_price(age)
    if ticket_cost == 0:
        print(f"Age: {age} No Ticket")

    else:
        print(f"Age: {age} Ticket: ${ticket_cost}")

        # checks payment method (cash or credit)
        pay_method = choice_checker("How Would You Like To Pay \n(credit surcharge 5%): ", cash_credit, "Please Choose A Valid Payment Method", 2)
        print(pay_method)
        
        if pay_method == "credit":
            surcharge = ticket_cost * 0.05
        
        else:
            surcharge = 0
        
        all_names.append(ask_name)
        all_ages.append(age)
        all_ticket_costs.append(ticket_cost)
        surcharge_list.append(surcharge)
        
mini_movie_frame = pd.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index("Name")

# calculate ticket cost
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# calculate profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# calculate ticket/profit total
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

# get today's date
today = date.today()

# get day/month/year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"=== Mini Movie Fundraiser Ticket Data {day}/{month}/{year} ===\n"
filename = f"MMF_{year}_{month}_{day}"

add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# change frame to string so it can be exported
mini_movie_string = pd.DataFrame.to_string(mini_movie_frame)

ticket_cost_heading = "\n===== Ticket Cost/Profit ====="
total_ticket_sales = "Total Ticket sales: ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}\n".format(profit)

# choose a raffle winner
raffle_winner = rd.choice(all_names)
winner_heading = "\n=== Raffle Winner ==="
winner_text = f"Congrats [{raffle_winner}]. You Have Won The Raffle i.e Your Ticket is free!\n"

# prints amount of tickets sold/remaining
tickets_remaining = tickets_total - tickets_sold
if tickets_remaining == 0:
    sold_status = "Congrats You Have Sold All Tickets"
else:
    sold_status = f"You Have Sold {tickets_sold} Ticket/s. You Have {tickets_remaining} Ticket/s Remaining"

to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sold_status, winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()