# Define the menu and resources available
MENU = {
    "espresso": {"water": 50, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
}

profit = 0
resources = {"water": 300, "milk": 200, "coffee": 100}

def print_report():
    """Print the current resource values and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(drink):
    """Check if there are enough resources to make the drink."""
    for item in MENU[drink]:
        if item != "cost" and MENU[drink][item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_payment(cost):
    """Process coin payment and return whether it's successful."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    if total >= cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink):
    """Deduct the required ingredients from the resources and serve the coffee."""
    for item in MENU[drink]:
        if item != "cost":
            resources[item] -= MENU[drink][item]
    print(f"Here is your {drink} ☕️. Enjoy!")

# Main loop to run the coffee machine
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print_report()
    elif choice in MENU:
        if check_resources(choice):
            if process_payment(MENU[choice]["cost"]):
                make_coffee(choice)
    else:
        print("Invalid choice. Please choose again.")
