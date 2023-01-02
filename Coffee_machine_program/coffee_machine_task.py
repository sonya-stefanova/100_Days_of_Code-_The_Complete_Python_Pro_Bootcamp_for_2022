from menu import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(payment, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(selected_drink, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {selected_drink} ☕️. Enjoy!")


machine_is_on = True

while machine_is_on:
    order = input("💁‍What would you like? (espresso/latte/cappuccino/turn off/report): ")
    if order == "turn off":
        machine_is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        selected_drink = MENU[order] #espresso/latte/cappuccino
        if is_resource_sufficient(selected_drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, selected_drink["cost"]):
                make_coffee(selected_drink=order, order_ingredients=selected_drink["ingredients"])








