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
    },
}

resources = {
    "water": {"quantity": 300, "unit": "ml"},
    "milk": {"quantity": 200, "unit": "ml"},
    "coffee": {"quantity": 100, "unit": "g"},
}


def resources_check(selection, resources):
    for ingredient in resources:
        if ingredient in MENU[selection]["ingredients"] and (
            MENU[selection]["ingredients"][ingredient]
            > resources[ingredient]["quantity"]
        ):
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def payment_input():
    print("Please insert coins.")
    money_sum = 0
    money_sum += int(input(f"How many quarters?:")) * 0.25
    money_sum += int(input(f"How many dimes?:")) * 0.1
    money_sum += int(input(f"How many nickles?:")) * 0.05
    money_sum += int(input(f"How many pennies?:")) * 0.01
    print(money_sum)
    return money_sum


def resources_update(selection, resources):
    for ingredient in MENU[selection]["ingredients"]:
        resources[ingredient]["quantity"] -= MENU[selection]["ingredients"][ingredient]


while True:
    selection = input("What would you like? (espresso/latte/cappuccino):")

    if selection in ["espresso", "latte", "cappuccino"]:
        if resources_check(selection, resources):
            money_received = payment_input()
            if money_received >= MENU[selection]["cost"]:
                print(
                    "Here is ${:0.2f} dollars in change".format(
                        money_received - MENU[selection]["cost"]
                    )
                )
                resources_update(selection, resources)
                print(f"Here is your {selection}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif selection == "report":
        for key in resources:
            print(f"{key}: {resources[key]['quantity']}{resources[key]['unit']}")
    elif selection == "off":
        break
