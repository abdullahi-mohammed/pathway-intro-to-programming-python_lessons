# Author: Abdullahi Mohammed
# Date:   18th, jan. 2024.
# Purpose: Meal price calculator
# Stretch Challenge: i added drinks in addition to the meal.

print("")
# What is the price of a child's meal? 4.50
child_meal_price = float(input("What is the price of a child's meal? "))
# What is the price of a child's drink? 2.0
child_drink_price = float(input("What is the price of a child's drink? "))
# What is the price of an adult's meal? 9.00
adult_meal_price =  float(input("What is the price of an adult's meal? "))
# What is the price of an adult's drink? 5.00
adult_drink_price =  float(input("What is the price of an adult's drink? "))
# How many children are there? 4
children_num =  int(input("How many children are there? "))
# How many adults are there? 2
adult_num =  int(input("How many adults are there? "))
print("")

# Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal, and multiplying the number of adults by the price of their meal and adding those two values together.
meal_subtotal = (children_num * child_meal_price) + (adult_num * adult_meal_price) + (children_num * child_drink_price) + (adult_num * adult_drink_price)
# Subtotal: $36.00
print(f"Subtotal: ${round(meal_subtotal, 2)}")
print("")

# Ask the user for the sales tax rate as a percentage (floating point). Please note that this percentage should be entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.
# What is the sales tax rate? 6
sales_tax_rate = float(input("What is the sales tax rate? "))

# Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
# Sales Tax: $2.16
sales_tax = (meal_subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${round(sales_tax, 2)}")

# Compute and display the total price of the meal by adding the subtotal and the sales tax.
# Total: $38.16
total_price = meal_subtotal + sales_tax
print(f"Total: ${total_price}")
print("")
# What is the payment amount? 40
payment_amount = float(input("What is the payment amount? "))
# Change: $1.84
change = payment_amount - total_price
print(f"Change: ${round(change, 2)}")
print("")