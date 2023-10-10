# The code is a simple tip calculator program written in Python.
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
print(
    "Each person should pay: $"
    + str(round(bill * (1 + (float(percentage) / 100)) / people, 2))
)
