MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
def resources_reformatted():
    print(f"water: {resources["water"]} ml")
    print(f"milk: {resources["milk"]} ml ")
    print(f"coffee: {resources["coffee"]} gramm")
    print(f"money: {money}$")
def money_amount():
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many quarters?:"))
    nickles = int(input("How many quarters?:"))
    pennies = int(input("How many quarters?:"))
    return quarters * 0.25 + dimes * 0.1 + nickles*0.05 + pennies * 0.01

def is_resource_sufficient(user_choice):
    water = MENU[user_choice]["ingredients"]["water"]
    milk = MENU[user_choice]["ingredients"]["milk"]
    coffee = MENU[user_choice]["ingredients"]["coffee"]
    if resources["water"] >= water and resources["milk"] >= milk and resources["coffee"] >= coffee:
        return True
    else:
        return False



money = 0
is_the_end = False
while not is_the_end:
    inserted_money = 0
    user_choice = input("What would you like? espresso/latte/cappucino or type 'close' to exit:")
    is_sufficient = is_resource_sufficient(user_choice)
    if is_sufficient:
        inserted_money = money_amount()
        if inserted_money >= MENU[user_choice]["cost"]:
            resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
            print(f"Here is your {user_choice}")
            print(f"This is your change {round(inserted_money - MENU[user_choice]["cost"], 2)}")
            money += MENU[user_choice]["cost"]
        else:
            print("Money is insufficient!")
            is_the_end = True
    else:
        print("Sorry, resource isn't sufficient")
        is_the_end = True
    report = input("Do you need a report? Type 'y' or 'n':")
    if report == "y":
        print(resources_reformatted())


# user_choice = input("What would you like? espresso/latte/cappucino:")
# if user_choice == "report":
#     resources_reformatted()
