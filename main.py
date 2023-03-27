from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#drink = MenuItem()
available_drink = Menu()
waiter = CoffeeMaker()
cashier = MoneyMachine()

x = available_drink.get_items()
dispense = True
while dispense:
    user_input = input(f"What would you like? ({x}): ").lower()
    if user_input in x:
        order = available_drink.find_drink(user_input)
        sufficient = waiter.is_resource_sufficient(order)
        if sufficient:
            payment_accepted = cashier.make_payment(order.cost)
            if payment_accepted:
                waiter.make_coffee(order)
    elif user_input == "off":
        dispense = False
    elif user_input == "report":
        waiter.report()
        cashier.report()
