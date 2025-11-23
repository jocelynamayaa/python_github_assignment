print("Welcome to my Python program!") # Task 1 - Welcome Message

savings = input("How much money did you save this month? ") # Task 2 - Asks the user for input

savings = float(savings) # Task 3 - Converts input to float
yearly_savings = savings * 12 # Performs calculation for the year

print(f"At this saving rate, you will save ${yearly_savings:.2f} in a year.") # Task 4 - Displays the result clearly

# Task 5 - Error handling for non-numeric input
try:
    saving = float(input("How much money did you save this month? "))
except ValueError: 
    print("Please enter a valid number.")
    exit()