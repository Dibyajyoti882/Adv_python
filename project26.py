#Restaurant Billing System Display a menu with prices and allow users to order multiple items. Calculate the total bill with tax. Use loops for ordering, dictionaries for storing menu, and conditionals for bill logic.
menu = {"tea": 10, "coffee": 20, "burger": 50}

total = 0

while True:
    item = input("Enter item (or stop): ")
    if item == "stop":
        break
    if item in menu:
        total += menu[item]

tax = total * 0.1
print("Total:", total + tax)