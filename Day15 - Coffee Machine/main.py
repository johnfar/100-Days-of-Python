MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffee_machine():


    user_input = ""
    while user_input != "off":
        print("What would you like? (espresso/latte/cappuccino): ")
        user_input = input()
        if user_input.lower() == "report":
            report()
        elif user_input.lower() == "espresso" or user_input.lower() == "latte" or user_input.lower() == "cappuccino":
            resources_available, water, milk, coffee, cost = resourceChecker(user_input.lower())
            print(resources_available)
            if resources_available:
                user_entered_amount = proccess_coins()
                print(check_transaction(cost, user_entered_amount))
                print(MENU["Money"])
                make_coffee(user_input, water, milk, coffee)


# Print Report
def report():
    for k, v in resources.items():
        print(f"{k.title()}: {v}" )

# Check for sufficent resources

def resourceChecker(item):
    print(MENU[item])
    cost = MENU[item]["cost"]
    if "water" in MENU[item]["ingredients"]:
        water = MENU[item]["ingredients"]["water"]
        if water > resources["water"]:
            print("Sorry there is not enough water")
            return False

    if "milk" in MENU[item]["ingredients"]:
        milk = MENU[item]["ingredients"]["milk"]
        if milk > resources["milk"]:
            print("Sorry there is not enough milk")
            return False

    if "coffee" in MENU[item]["ingredients"]:
        coffee = MENU[item]["ingredients"]["coffee"]
        if coffee > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
    return True, water, milk, coffee, cost

    


# Process COins

def proccess_coins():
    print("Please insert coins.")
    print("How many quarters? ")
    quarters_added = input()
    print("How many dimes? ")
    dimes_added = input()
    print("How many nickels? ")
    nickels_added = input()
    print("How many pennies? ")
    pennies_added = input()
    total_amount_added = (int(quarters_added) * 0.25) + (int(dimes_added) * 0.1) + (int(nickels_added) * 0.05) + (int(pennies_added) * 0.01)
    return total_amount_added


# Check transaction successful
def check_transaction(cost, user_amount_entered):
    if cost > user_amount_entered:
        print("Sorry that's not enough money.  Money refunded.")
        return False
    else:
        if cost < user_amount_entered:
            print("Here is $%2d dollars in change" % (user_amount_entered - cost))
        if "Money" in MENU:
            MENU["Money"] = MENU["Money"] + cost
        else:
            MENU["Money"] = cost
        return True

# Make Coffee
def make_coffee(item, water, milk, coffee):
    MENU[item]["ingredients"]["water"] = MENU[item]["ingredients"]["water"] - water
    MENU[item]["ingredients"]["milk"] = MENU[item]["ingredients"]["milk"] - milk
    MENU[item]["ingredients"]["coffee"] = MENU[item]["ingredients"]["coffee"] - coffee
    print("Here is your %s. Enjoy!" %item)

coffee_machine()