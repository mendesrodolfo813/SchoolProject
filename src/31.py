import math

def calculate_total_cost(hours):
    total_cost = hours * 100.0
    return total_cost

hours = int(input("Enter the number of hours worked: "))
total_cost = calculate_total_cost(hours)
print(f"The total cost for {hours} hours is ${total_cost:.2f}")
