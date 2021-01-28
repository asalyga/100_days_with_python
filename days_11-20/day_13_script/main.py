from assets import resources, MENU


def update_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    resources["money"] += MENU[drink]["cost"]


def resources_check(drink):
    ing_water = MENU[drink]["ingredients"]["water"]
    if drink != "espresso":
        ing_milk = MENU[drink]["ingredients"]["milk"]
    ing_coffee = MENU[drink]["ingredients"]["coffee"]
    res_water = resources["water"]
    res_milk = resources["milk"]
    res_coffee = resources["coffee"]
    if res_water <= ing_water:
        print("Sorry there is not enough Water")
    elif drink != "espresso":
        if res_milk <= ing_milk:
            print("Sorry there is not enough Milk")
    elif res_coffee <= ing_coffee:
        print("Sorry there is not enough Coffee")
    else:
        return 1


def process_coins(drink):
    cost = MENU[drink]["cost"]
    coins = 0.0
    quarters = float(input("How many quarters? :"))
    coins += quarters * 0.25
    dimes = float(input("How many dimes? :"))
    coins += dimes * 0.10
    nickles = float(input("How many nickles? :"))
    coins += nickles * 0.05
    pennies = float(input("How many pennies? :"))
    coins += pennies * 0.01
    if coins >= cost:
        print(f"Here is ${round(coins - cost, 2)} in change.")
        return 1
    else:
        print(f"Sorry, that's not enough money!. Refunded ${coins}")


def espresso():
    drink = "espresso"
    if resources_check(drink):
        if process_coins(drink):
            update_resources(drink)
            print(f"Here is your {drink}. Enjoy!")


def latte():
    drink = "latte"
    if resources_check(drink):
        if process_coins(drink):
            update_resources(drink)
            print(f"Here is your {drink}. Enjoy!")


def cappuccino():
    drink = "cappuccino"
    if resources_check(drink):
        if process_coins(drink):
            update_resources(drink)
            print(f"Here is your {drink}. Enjoy!")


def report():
    print(f'Water: {resources["water"]}ml'
          f'\nMilk: {resources["milk"]}ml'
          f'\nCoffee: {resources["coffee"]}g'
          f'\nMoney: ${round(resources["money"], 2)}')


def take_order():
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order == "espresso":
            espresso()

        if order == "latte":
            latte()

        if order == "cappuccino":
            cappuccino()

        if order == "report":
            report()

        if order == "quit":
            quit()


take_order()
