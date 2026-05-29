MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18,},
        "cost": 1.5,},
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24,},
        "cost": 2.5,},
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24,},
        "cost": 3.0,}
}

resources = {"water": 300, "milk": 200, "coffee": 100, }

def cost(coffee):
    money_to_be_paid = MENU[coffee]["cost"]
    print(f"cost: ${money_to_be_paid}")
    return money_to_be_paid

money_earned = 0

water_initial= resources["water"]
milk_initial= resources["milk"]
coffee_initial= resources["coffee"]

water_consumed=0
milk_consumed=0
coffee_consumed=0

water_left=None
milk_left=None
coffee_left=None

def water_available(initial, consumed):
    water= initial - consumed
    return water

def milk_available(initial, consumed):
    milk = initial - consumed
    return milk

def coffee_available(initial, consumed):
    coffee = initial - consumed
    return coffee

next_order = True
while next_order:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    water_left = water_available(water_initial, water_consumed)
    milk_left = milk_available(milk_initial, milk_consumed)
    coffee_left = coffee_available(coffee_initial, coffee_consumed)

    if user_choice=="off":
        next_order=False

    elif user_choice == "report":
        print(f"Water: {water_left}ml")
        print(f"Milk: {milk_left}ml")
        print(f"Coffee: {coffee_left}g")
        print(f"Money: ${money_earned}")

    else:
        water_required = MENU[f"{user_choice}"]["ingredients"]["water"]
        if "milk" not in MENU[f"{user_choice}"]["ingredients"]:
            milk_required = 0
        else:
            milk_required = MENU[f"{user_choice}"]["ingredients"]["milk"]
        coffee_required = MENU[f"{user_choice}"]["ingredients"]["coffee"]

        if water_required > water_left:                     #compare ingredient required and ingredient left
            print("Sorry, there is not enough water.")
        elif milk_required > milk_left:
            print("Sorry, there is not enough milk.")
        elif coffee_required > coffee_left:
            print("Sorry, there is not enough coffee.")
        else:
            coffee_cost = cost(user_choice)
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            money_paid = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

            if money_paid < coffee_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                water_consumed += water_required
                milk_consumed += milk_required
                coffee_consumed += coffee_required

                balance = money_paid - coffee_cost
                print(f"Here is ${balance:.2f} in change.")
                money_earned += coffee_cost
                print(f"Here is your {user_choice}☕. Enjoy!")
