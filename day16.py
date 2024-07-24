############### classes attributes and methods in python ##################

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

# Accessing attributes and calling methods
print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Civic

car1.display_details()  
car2.display_details() 
 

 ######################## Cofee machine project in classes  ######################
class CoffeeMachine:
    MENU = {
        "espresso": {"water": 50, "coffee": 18, "cost": 1.5},
        "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
        "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
    }

    def __init__(self):
        self.profit = 0
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def print_report(self):
        """Print the current resource values and profit."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.profit}")

    def check_resources(self, drink):
        """Check if there are enough resources to make the drink."""
        for item in self.MENU[drink]:
            if item != "cost" and self.MENU[drink][item] > self.resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_payment(self, cost):
        """Process coin payment and return whether it's successful."""
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickels?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_coffee(self, drink):
        """Deduct the required ingredients from the resources and serve the coffee."""
        for item in self.MENU[drink]:
            if item != "cost":
                self.resources[item] -= self.MENU[drink][item]
        print(f"Here is your {drink} ☕️. Enjoy!")

    def run(self):
        """Main loop to run the coffee machine."""
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                break
            elif choice == "report":
                self.print_report()
            elif choice in self.MENU:
                if self.check_resources(choice):
                    if self.process_payment(self.MENU[choice]["cost"]):
                        self.make_coffee(choice)
            else:
                print("Invalid choice. Please choose again.")


# Create a CoffeeMachine object and run it
coffee_machine = CoffeeMachine()
coffee_machine.run()


################## With multiple classes the code will be ####################

class Menu:
    def __init__(self):
        self.items = {
            "espresso": {"water": 50, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
        }

    def get_items(self):
        return self.items

    def is_item_available(self, item):
        return item in self.items


class PaymentProcessor:
    def __init__(self):
        self.profit = 0

    def process_payment(self, cost):
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickels?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def report_profit(self):
        print(f"Money: ${self.profit}")


class CoffeeMachine:
    def __init__(self):
        self.menu = Menu()
        self.payment_processor = PaymentProcessor()
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def print_report(self):
        """Print the current resource values and profit."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        self.payment_processor.report_profit()

    def check_resources(self, drink):
        """Check if there are enough resources to make the drink."""
        for item in self.menu.get_items()[drink]:
            if item != "cost" and self.menu.get_items()[drink][item] > self.resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        """Deduct the required ingredients from the resources and serve the coffee."""
        for item in self.menu.get_items()[drink]:
            if item != "cost":
                self.resources[item] -= self.menu.get_items()[drink][item]
        print(f"Here is your {drink} ☕️. Enjoy!")

    def run(self):
        """Main loop to run the coffee machine."""
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                break
            elif choice == "report":
                self.print_report()
            elif self.menu.is_item_available(choice):
                if self.check_resources(choice):
                    if self.payment_processor.process_payment(self.menu.get_items()[choice]["cost"]):
                        self.make_coffee(choice)
            else:
                print("Invalid choice. Please choose again.")


# Create a CoffeeMachine object and run it
coffee_machine = CoffeeMachine()
coffee_machine.run()
