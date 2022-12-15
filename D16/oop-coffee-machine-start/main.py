from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
cash = MoneyMachine()


while True:
    options = menu.get_items()
    drink_selected = input(f"What would you like? {options}:")

    if drink_selected == "report":
        machine.report()
        cash.report()
    elif drink_selected == "off":
        break
    else:
        drink = menu.find_drink(drink_selected)
        if (
            drink is not None
            and machine.is_resource_sufficient(drink)
            and cash.make_payment(drink.cost)
        ):
            machine.make_coffee(drink)
