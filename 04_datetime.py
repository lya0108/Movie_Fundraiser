from datetime import date

# get today's date
today = date.today()

# get day/month/year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"the current date is {day}/{month}/{year}"
filename = f"MMF_{year}_{month}_{day}"

print(heading)
print(f"the filename will be {filename}.txt")