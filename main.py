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
end=False
while not end:
    def coffee():
        a = input("What would you like to have? espresso/latte/cappuccino: ").lower()
        print("Please insert coins:")
        b = int(input("How many quarters? "))
        c = int(input("How many dimes? "))
        d = int(input("How many nickels? "))
        e = int(input("How many cents? "))
        total = 0.25 * b + 0.10 * c + 0.05 * d + 0.01 * e
        if a in MENU:
            cost = MENU[a]["cost"]
            if cost > total:
                print("Not enough money. Your money is refunded.")
            else:
                for ingredient in MENU[a]["ingredients"]:
                    if resources[ingredient] < MENU[a]["ingredients"][ingredient]:
                        print(f"Sorry, there is not enough {ingredient}.")
                        break
                else:
                    for ingredient in MENU[a]["ingredients"]:
                        resources[ingredient] -= MENU[a]["ingredients"][ingredient]
                    balance=total-cost
                    print(f"Here is your {a}. Enjoy!")
                    print(f"Here is ${balance:.2f} in change.")
        elif a=="report":
            if b==c==d==e==1:
                 print(resources)
    coffee()
    l=input("Would you like to order again? yes/no ").lower()
    if l=="yes":
        coffee()
    elif l=="no":
        end=True
        print("Thanks for ordering")




