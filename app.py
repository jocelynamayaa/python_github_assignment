print("Welcome to my Python program!") # Welcome Message

# Error handling for non-numeric input
try:
    saving = float(input("How much money did you save this month? "))
except ValueError: 
    print("Please enter a valid number.")
    exit()

yearly_savings = saving * 12 # Calculates yearly savings

print(f"At this saving rate, you will save ${yearly_savings:.2f} in a year.") # Displays the result clear