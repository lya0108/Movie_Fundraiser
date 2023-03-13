import pandas as pd

def round(number):
    return "${:.2f}".format(number)

# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pd.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index("Name")

# calculate ticket cost
mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# calculate profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# calculate ticket/profit total
total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(round)


print("\n========== Ticket Data ==========")
print(mini_movie_frame)
print("\n===== Ticket Cost/Profit =====")

print("Total Ticket sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}\n".format(profit))