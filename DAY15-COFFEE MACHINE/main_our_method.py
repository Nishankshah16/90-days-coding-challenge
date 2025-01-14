from art import logo

print(logo)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 120.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200.10,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250.5,
    }
}

resources = {
    "water": 1000,
    "milk": 2000,
    "coffee": 500
} 

MONEY= 0

def report():
    return f"water: {resources['water']}\ncoffee: {resources["coffee"]}\nmilk: {resources["milk"]}\nmoney: {MONEY}$"

def check_ingredient(user_input):
    is_sufficient = True
    for i in MENU[user_input]["ingredients"]:
        
        if MENU[user_input]["ingredients"][i] > resources[i]:
            print(f"Sorry, no sufficient {i}")
            is_sufficient = False
    return is_sufficient

def despense(user_input):
    for i in MENU[user_input]["ingredients"]:
        resources[i] -= MENU[user_input]["ingredients"][i]

    print(f"Here is your {user_input}☕️")


def cost():
    print("Please insert the coins.")
    rupee=int(input("How many Rupee? "))
    paise=int(input("How many paisa? "))*0.01
    total = rupee + paise
    return total

    
    
def is_money_suff(total, user_input):
    money =True
    if total< MENU[user_input]["cost"]:
        print(f"No sufficient money , {total} money refunded")
        money = False
    else:
        total-= MENU[user_input]["cost"]
        round(total, 2)
        print(f"This is your Change {total}. ")
        global MONEY 
        MONEY += total
    return money

    

off= False
for i in MENU:
    print(i,":", MENU[i]["cost"] )
while not off:
    user_input=input("What would you like to have (espresso/latte/cappuccino): ").lower()
    if user_input in ("espresso","latte","cappuccino"):
        if check_ingredient(user_input):
            amt = cost()
            if is_money_suff(amt, user_input):
                despense(user_input)

    if user_input=='report':
        print(report())
    elif user_input=="off" or user_input == 'na':
        off= True
    print("\n" *20)







