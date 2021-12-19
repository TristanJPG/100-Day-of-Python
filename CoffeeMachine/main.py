#/usr/bin/python3
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
    "money": 0
} 
def start():
    p = input("​What would you like? (espresso/latte/cappuccino):​ ")
    if p == "report":
        report()
    if p == "espresso":
        espresso()
    if p == "latte":
        latte()
    if p == "cappuccino":
        cappuccino()
def end():
    print("Here is your drink ☕️. Enjoy!")
    start()
def report():
    for key, value in resources.items():
        print(key, ' : ', value)
    start()
def espresso():
    if resources["water"] < MENU["espresso"]["ingredients"]["water"] or resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
        print("We're sorry we do not have enough resourses to make your drink :(")
    else:
        up_Res_Esp = {
            "water": resources["water"] - MENU["espresso"]["ingredients"]["water"], 
        "coffee": resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"] 
        }
        resources.update({"water": up_Res_Esp["water"], "coffee": up_Res_Esp["coffee"]})
        transaction("espresso")
def latte():
    if resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["coffee"] < MENU["latte"]["ingredients"]["coffee"] or MENU["latte"]["ingredients"]["milk"]:
        print("We're sorry we do not have enough resourses to make your drink :(")
    else:
        up_Res_Esp = {
            "water": resources["water"] - MENU["latte"]["ingredients"]["water"], 
        "coffee": resources["coffee"] - MENU["latte"]["ingredients"]["coffee"],
        "milk": resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        }
        resources.update({"water": up_Res_Esp["water"], "coffee": up_Res_Esp["coffee"], "milk": up_Res_Esp["milk"]})
        transaction("latte")
def cappuccino():
    if resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"] or resources["milk"] < MENU["latte"]["ingredients"]["milk"] :
        print("We're sorry we do not have enough resourses to make your drink :(")
    else:
        up_Res_Esp = {
            "water": resources["water"] - MENU["cappuccino"]["ingredients"]["water"], 
        "coffee": resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"],
        "milk": resources["milk"] - MENU["latte"]["ingredients"]["milk"] 
        }
        resources.update({"water": up_Res_Esp["water"], "coffee": up_Res_Esp["coffee"]})
        transaction("cappuccino")
def transaction(item):
    print("Please Insert Coins")
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    quarter_amt = int((input("How many Quarters? ")))
    dime_amt = int(input("How many Dimes? "))
    nickel_amt = int(input("How many Nickles? "))
    penny_amt = int(input("How many Pennies? " ))
    money = (quarter * quarter_amt) + (dime * dime_amt) + (nickel * nickel_amt) + (penny * penny_amt)
    if item == "espresso": 
        if MENU["espresso"]["cost"] > money:
            print("This is not suffient change. Money Refunded..")
        if money >= MENU["espresso"]["cost"]:
            change = money - MENU["espresso"]["cost"]
            change = "{:.2f}".format(change)
            if str(change) <= "0":
                change = 0
            balance = resources["money"] + MENU["espresso"]["cost"]
            resources.update({"money": balance})
            print("Your change is $" + str(change))
            end()
    elif item == "latte": 
        if MENU["latte"]["cost"] > money:
            print("This is not suffient change. Money Refunded..")
        if money >= MENU["latte"]["cost"]:
            change = money - MENU["latte"]["cost"]
            change = "{:.2f}".format(change)
            if str(change) <= "0":
                change = 0
            balance = resources["money"] + MENU["latte"]["cost"]
            resources.update({"money": balance})
            print("Your change is $" + str(change))
            end()
    elif item == "cappuccino":
        if MENU["cappuccino"]["cost"] > money:
            print("This is not suffient change. Money Refunded..")
        if money >= MENU["cappuccino"]["cost"]:
            change = money - MENU["cappuccino"]["cost"]
            change = "{:.2f}".format(change)
            if str(change) <= "0":
                change = 0
            balance = resources["money"] + MENU["cappuccino"]["cost"]
            resources.update({"money": balance})
            print("Your change is $" + str(change))
            end()
start()






















