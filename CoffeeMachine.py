from CoffeeMachine_req import *


def __init__():

    who = input("Are you admin or user :: ")
    if who == "admin":
        topup()
    if who == "user":
        check_quantity()


def topup():

    water = int(input("how much water you want to top up (ml) :: "))
    quantity["water"] += water
    milk = int(input("how much milk you want to top up (ml) :: "))
    quantity["milk"] += milk
    coffee = int(input("how much coffee you want to top up (ml) :: "))
    quantity["coffee"] += coffee


def get_user_coffee():
    
    coffee = input("what coffee do you want ? espresso/latte/cappuccino :: ")
    
    for i in Menu:
        if coffee == i:
            for y in Menu[i]:
                if y == "cost":
                    print(f"price : {Menu[i][y]}")
                    price = Menu[i][y]
            #print(Menu[i])
    return (price, Menu[coffee])


def check_make_coffee(total):

    price,menu = get_user_coffee()

    if total >= price:
        print(f"success :: {total} > {price}")
        print(f"Menu is :: {menu}")
        
        if quantity["water"] < menu['ingredients']['water'] or quantity["milk"] < menu['ingredients']['milk'] or quantity["coffee"] < menu['ingredients']['coffee']: 
            print("less quantity of Ingridient please choose nother")
            check_make_coffee(total)
            
        else:
            return_to_user = total - price
                
            water = menu['ingredients']['water']
            if quantity["water"] - water < 0 :
                print("Less water for this order admin needs to top up the order !! ")
                topup()
            else:
                quantity["water"] = quantity["water"] - water 

            milk = menu['ingredients']['milk']
            if quantity["milk"] - milk < 0 :
                print("Less milk for this order admin needs to top up the order !! ")
                topup()
            else :
                quantity["milk"] = quantity["milk"] - milk 

            coffee = menu['ingredients']['coffee']
            if quantity["coffee"] - coffee < 0 :
                print("Less milk for this order admin needs to top up the order !! ")
                topup()
            else :
                quantity["coffee"] = quantity["coffee"] - coffee

            print(f"{quantity['water']}, {quantity['milk']}, {quantity['coffee']}")


            quantity["money"] = quantity["money"] + price
            print(f"{quantity['money']}")

            print(f"your change :: {return_to_user}")

            print("succcccessssss")
            print(quantity)

    else:
        return_to_user = total
        print(f"fail - the amount paid is less {return_to_user}")
        return False
    

def coins_calc():

    print("Please insert coins :: ")
    rupee100 = int(input("how many rupee 100 :: "))
    rupee100 = coins["rupee100"] * rupee100

    rupee50 = int(input("how many rupee 50 :: "))
    rupee50 = coins["rupee50"] * rupee50

    rupee20 = int(input("how many rupee 20 :: "))
    rupee20 = coins["rupee20"] * rupee20

    rupee10 = int(input("how many rupee 10 :: "))
    rupee10 = coins["rupee10"] * rupee10

    total = (rupee100 + rupee50 + rupee20 + rupee10)
    #print(f"total coins inserted : {total}")

    return total


def check_quantity():

    print(quantity)

    total = coins_calc()
    print(total)

    if quantity["water"] >= 50 and quantity["milk"] >= 0 and quantity["coffee"] >= 18:
        if total > 150:
            print("resource available to make coffe ")
            check_make_coffee(total)
            
        else: 
            print("amount is less than the minimum order")

    else:
        print("resource less cannot make coffe")
        return_to_user = total
        print(f"fail - Amount refund back :: {return_to_user}")
        topup()


machine_on = True

while machine_on:
    __init__()

    








