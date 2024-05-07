# Author: Abdullahi Mohammed
# Date:   9th, feb. 2024.
# Purpose: Shopping Cart Program
# Stretch Challenge: I added a program that allowed the user to specify the quantity of products they want and also made sure that i calculated the correct total amount of item of quantity added.

# Welcome to the Shopping Cart Program!

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 1
# What item would you like to add? Milk
# What is the price of 'Milk'? 3.49
# 'Milk' has been added to the cart.

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 1
# What item would you like to add? Bread
# What is the price of 'Bread'? 2.50
# 'Bread' has been added to the cart.

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 1
# What item would you like to add? Butter
# What is the price of 'Butter'? 4.00
# 'Butter' has been added to the cart.

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 2
# The contents of the shopping cart are:
# 1. Milk - $3.49
# 2. Bread - $2.50
# 3. Butter - $4.00

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 3
# Which item would you like to remove? 2
# Item removed.
# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 2
# The contents of the shopping cart are:
# 1. Milk - $3.49
# 2. Butter - $4.00

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 4
# The total price of the items in the shopping cart is $7.49

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 5
# Thank you. Goodbye.


shopping_cart = []

print("Welcome to the Shopping Cart Program!\n")
# print("")

status = "ON"

while status == "ON":
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action: ")
    if action == "1":
        add_item = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{add_item}'? "))
        item_qtty = int(input(f"How many quantity of '{add_item}'? "))
        # if item_price != "":
        #     float(item_price)
        shopping_cart.append([add_item, item_price, item_qtty])
        print(f"'{add_item}' has been added to the cart.\n")
    elif action == "2":
        print("The contents of the shopping cart are:")
        for i, item in enumerate(shopping_cart):
            print(f"{i + 1}. {item[0]} - ${item[1]:.2f}, quantity: {item[2]}")
        print("")    
    elif action == "3": 
        remove_item = int(input("Which item would you like to remove? "))
        del shopping_cart[remove_item - 1]
        print("Item removed.\n")
    elif action == "4":
        total_price = 0
        for item in shopping_cart:
            total_price += (item[1] * item[2])
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}\n")
    elif action == "5":
        print("Thank you. Goodbye.")
        status = "OFF"
    else:
        print("Sorry, that is not a valid item number.")