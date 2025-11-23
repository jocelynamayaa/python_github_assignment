print("Welcome to my Python program!")

savings = input("How much money did you save this month? ")

savings = float(savings)
yearly_savings = savings * 12

print(f"At this saving rate, you will save ${yearly_savings:.2f} in a year.")