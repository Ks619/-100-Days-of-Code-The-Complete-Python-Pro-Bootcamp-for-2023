""""Instructions in CoffeeMachine_instructions.pdf """
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


def get_input() -> str:
    """Gets the input from the user"""
    user_input = str(input("What would you like? (espresso/latte/cappuccino):\n"
                           "For report press 'report'\n"
                           "To close the coffee machine press 'off'\n"))

    while user_input != "espresso" and user_input != "latte" and user_input != "cappuccino" and user_input != "report" \
            and user_input != "off":
        print("What would you like? (espresso/latte/cappuccino):")
        print("To close the coffee machine press 'off'")
    return user_input


def print_report(cash) -> None:
    """Prints the report of all the remaining ingredients"""
    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney: {cash}")


def enough_resources(chosen_drink) -> str:
    """Returns 'Yes' if there is enough ingredients to make the chosen drink, or 'No' if there isn't enough
    ingredients to make the chosen drink """
    if resources['water'] < MENU[chosen_drink]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return "No"
    if chosen_drink != "espresso" and resources['milk'] < MENU[chosen_drink]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return "No"
    if resources['coffee'] < MENU[chosen_drink]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return "No"
    return "Yes"


def how_much_money() -> float:
    """Returns How much money the user inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 25 + nickles * 5 + dimes * 10 + pennies * 1) / 100
    return total


def set_resources(chosen_drink) -> None:
    """Update the resources after making a coffee"""
    if chosen_drink == "espresso":
        resources['water'] -= MENU[chosen_drink]['ingredients']['water']
        resources['coffee'] -= MENU[chosen_drink]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[chosen_drink]['ingredients']['water']
        resources['milk'] -= MENU[chosen_drink]['ingredients']['milk']
        resources['coffee'] -= MENU[chosen_drink]['ingredients']['coffee']


flag = True
check_resources = ""
check_money = 0
money = 0

while flag:
    drink = get_input()
    if drink == "off":
        flag = False
        break
    if drink == "report":
        print_report(money)
        continue

    check_resources = enough_resources(drink)
    if check_resources == "No":
        continue

    check_money = how_much_money()
    if MENU[drink]['cost'] == check_money:
        print(f"Here is your {drink}. Enjoy")
        money += MENU[drink]['cost']
        set_resources(drink)

    elif MENU[drink]['cost'] < check_money:
        print(f"Here is your {drink}. Enjoy")
        print(f"Here is ${check_money - MENU[drink]['cost']} dollars in change")
        money += MENU[drink]['cost']
        set_resources(drink)
    else:
        print("Sorry that's not enough money. Money refunded.")
