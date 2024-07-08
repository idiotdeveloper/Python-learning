
'''
this is a simple calculator but with the following concepts : 
    Dictionary
    function return
    Recursion 
'''


def add (n1, n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mul (n1, n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2 


operations = { 

    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculation():

    num1 = float(input("enter the first numner : "))
    num2 = float(input("enter the second numner : "))

    for dict in operations:
        print(dict)

    cont = True
    while cont: 
        operation_pick = input("pick an operation from the line above : ")
        calc = operations[operation_pick]
        result = calc(num1, num2)
        print(f"num1 : {num1} {operation_pick} num2: {num2} =", result)

        new_input = input("do you want to continue : y and to start a fresh calculation : n and any other key to exit ::: ")

        if new_input == "y":
            num3 = float(input("enter the next numner : "))
            num1 = result
            num2 = num3

        elif new_input == "n":
            cont = False  # any way not required becase the function is called from the begining and it value will be set to true because of recursion. 
            calculation() #recursion function. 

        else:
            exit()

calculation()




'''while cont:
    
    if new_input == "y":
        num3 = int(input("enter the another numner : "))
        operation_pick = input("pick an operation from the line above : ")
        calc = operations[operation_pick]
        result = calc(result, num3)
        print(result)

    else:
        cont = False
'''







    






