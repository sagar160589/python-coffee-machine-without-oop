from art import coffee,coffee_machine
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

coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

coffee_machine_off = False
cost = 0

print(coffee_machine)


def calculate_cost_after_coins_insert(user_inserted_coins, coffee_cost):
    allowed_to_get_coffee = False
    if user_inserted_coins >= coffee_cost:
        if user_inserted_coins > coffee_cost:
            change = round(user_inserted_coins - coffee_cost,2)
            print(f"Here is ${change} in change")
        allowed_to_get_coffee = True

    else:
        print("Sorry That's not enough money. Money refunded")
        allowed_to_get_coffee = False
    return allowed_to_get_coffee


def insert_coins(coffee_cost):
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    return calculate_cost_after_coins_insert((coins["quarters"]*quarters)+(coins["dimes"]*dimes)+
                                      (coins["nickles"]*nickles)+(coins["pennies"]*pennies), coffee_cost)


def deplete_resources(coffee_type, report):
    if coffee_type == 'espresso':
        water_remained = report['water'] - MENU[coffee_type]['ingredients']['water']
        coffee_remained = report['coffee'] - MENU[coffee_type]['ingredients']['coffee']
        resources['water'] = water_remained
        resources['coffee'] = coffee_remained
    else:
        water_remained = report['water'] - MENU[coffee_type]['ingredients']['water']
        coffee_remained = report['coffee'] - MENU[coffee_type]['ingredients']['coffee']
        milk_remained = report['milk'] - MENU[coffee_type]['ingredients']['milk']
        resources['water'] = water_remained
        resources['coffee'] = coffee_remained
        resources['milk'] = milk_remained


def check_resources(coffee_type):
    global cost
    if coffee_type == 'espresso':
        if MENU[coffee_type]['ingredients']['water'] < resources['water']:
            if MENU[coffee_type]['ingredients']['coffee'] < resources['coffee']:
                print("Please insert coins")
                allowed_to_get_coffee = insert_coins(MENU[coffee_type]["cost"])
                if allowed_to_get_coffee:
                    deplete_resources(coffee_type,resources)
                    cost += MENU[coffee_type]["cost"]
                    print(f"Here is your {coffee_type} {coffee}. Enjoy!")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    elif coffee_type == 'report':
        resources['Money'] = cost
        for r in resources:
            if r == 'Money':
                print(f"{r}: ${resources[r]}")
            else:
                print(f"{r}: {resources[r]}")
    elif coffee_type == 'latte' or coffee_type == 'cappuccino':
        if MENU[coffee_type]['ingredients']['water'] < resources['water']:
            if MENU[coffee_type]['ingredients']['coffee'] < resources['coffee']:
                if MENU[coffee_type]['ingredients']['milk'] < resources['milk']:
                    print("Please insert coins")
                    allowed_to_get_coffee = insert_coins(MENU[coffee_type]["cost"])
                    if allowed_to_get_coffee:
                        deplete_resources(coffee_type, resources)
                        cost += MENU[coffee_type]["cost"]
                        print(f"Here is your {coffee_type} {coffee}. Enjoy!")
                    else:
                        print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    elif coffee_type == 'off':
        print("Coffee Machine down for maintenance. Please try after some time. Thank you!")
        global coffee_machine_off
        coffee_machine_off = True
    else:
        print("Invalid input.. No such coffee or report exists. Please try again")


while not coffee_machine_off:
    check_resources(input("What would you like? (espresso/latte/cappuccino): "))

