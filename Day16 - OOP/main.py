import coffee_maker
import menu
import money_machine

def run():
    switch_on = True
    coffe_machine = coffee_maker.CoffeeMaker()
    drink_menu = menu.Menu()
    process_money = money_machine.MoneyMachine()
    while switch_on:

        user_input = input(f"What would you like? ({drink_menu.get_items()}): ")
        if user_input.lower() == "off":
            switch_on = False
        elif user_input.lower() == "report":
            coffe_machine.report()
            process_money.report()
        else:
            item = drink_menu.find_drink(user_input.lower())
            if item == None:
                pass
            else:
                if coffe_machine.is_resource_sufficient(item):
                    is_paid = process_money.make_payment(item.cost)
                    if is_paid:
                        coffe_machine.make_coffee(item)            
        
run()