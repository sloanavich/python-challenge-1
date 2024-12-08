# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
customer_order = []
print(customer_order)

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key                                     #what is this doing? and why?
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_selection = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():
            # Save the menu category name to a variable
            menu_selection_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            print(f"You selected {menu_selection_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_selection_name} item would you like to order?")
            i = 1
            menu_items = {}                                         
            print("Item # | Item Name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_selection_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item Name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:                                               
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item Name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            submenu_selection_num = input("Enter menu item number: ")      #
            # 3. Check if the customer typed a number
            if submenu_selection_num.isdigit():                            #
                # Convert the menu selection to an integer
                submenu_selection_num = int(submenu_selection_num)              #
                # 4. Check if the menu selection is in the menu items
                if submenu_selection_num in menu_items.keys():         #

                    # Store the item name as a variable
                    submenu_item_name = menu_items[submenu_selection_num]["Item Name"]
                    submenu_item_price = menu_items[submenu_selection_num]["Price"]

                    # Ask the customer for the quantity of the menu item
                    item_quantity = input("How many would you like? ")  #

                    # Check if the quantity is a number, default to 1 if not
                    if item_quantity.isdigit():                         #
                        item_quantity = int(item_quantity)
                    else:
                        item_quantity = 1                             #

                    # Add the item name, price, and quantity to the order list
                    customer_order.append({
                        "Item Name" : submenu_item_name,                    #
                        "Price" : submenu_item_price,
                        "Quantity" : item_quantity,
                    })
                    # Tell the customer that their input isn't valid
                else:
                    print(f"{submenu_selection_num} is not on the menu.")          #

                # Tell the customer they didn't select a menu option
            else:
                print("Please enter a valid menu number option.")             #
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():                #
                # Keep ordering
            case "y":                                 #
                break                               #
                # Exit the keep ordering question loop
            case "n":                                  #
                # Complete the order
                place_order = False                     #
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order.")       #
                # Exit the keep ordering question loop
                break                                   #

                # Tell the customer to try again
            case _:                                 #
                print("Please try again.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in customer_order:
    # 7. Store the dictionary items as variables
    item_name = item["Item Name"]
    item_price = item["Price"]
    item_quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    item_name_spaces = 26 - len(item_name)
    item_price_spaces = 8 - len(str(item_price))
    item_quantity_spaces = 10 - len(str(item_quantity))

    # 9. Create space strings
    name_space_str = " " * item_name_spaces 
    price_space_str = " " * item_price_spaces
    quantity_space_str = " " * item_quantity_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_space_str}|{item_price}{price_space_str}|{item_quantity}{quantity_space_str}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum([item["Price"] * item["Quantity"] for item in customer_order])
print(f"Your total comes to ${total_cost}")