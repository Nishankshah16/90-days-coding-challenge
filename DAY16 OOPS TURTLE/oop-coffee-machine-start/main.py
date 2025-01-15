from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
mm = MoneyMachine()
cm=CoffeeMaker()
print(menu.get_items())
off = True
while off:
    user_input=input("What would you like to have espresso/latte/capaccino ").lower()
    if user_input== 'report':
        cm.report()
        mm.report()
    elif user_input =='off':
        off = False
    else:
        drink =menu.find_drink(user_input)

        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)



