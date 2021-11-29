import util


def fetch_report():
    print(f"Water: {util.resources['water']}")
    print(f"Milk: {util.resources['milk']}")
    print(f"Coffee: {util.resources['coffee']}")
    ask_user()


def check_resources(drink):
    if drink == 'cappuccino' or drink == 'latte':
        if util.resources['milk'] < util.MENU[drink]['ingredients']['milk']:
            print("Sorry!! Not sufficient milk")
            ask_user()
    if util.resources['water'] < util.MENU[drink]['ingredients']['water']:
        print("Sorry!! Not sufficient water")
        ask_user()
    elif util.resources['coffee'] < util.MENU[drink]['ingredients']['coffee']:
        print("Sorry!! Not sufficient coffee")
        ask_user()
    else:
        return


def update_resources(drink):
    util.resources['water'] -= util.MENU[drink]['ingredients']['water']
    if drink=='latte' or drink=='cappuccino':
        util.resources['milk'] -= util.MENU[drink]['ingredients']['milk']
    util.resources['coffee'] -= util.MENU[drink]['ingredients']['coffee']


def ask_user():
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == 'report':
        fetch_report()
    if drink == 'off':
        exit(0)
    check_resources(drink)
    money = ask_money()
    if money < util.MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        ask_user()
    else:
        update_resources(drink)
        change = money-util.MENU[drink]['cost']
        print(f"Here's ${change} in change")
        print(f"Here's your {drink} enjoy")
        ask_user()


def ask_money():
    print("Please insert coins.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickels = int(input("how many nickels?"))
    pennies = int(input("how many pennies?"))
    money = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    return money


ask_user() 