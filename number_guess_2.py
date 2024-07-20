import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

rand = random.randint(1,100)

print(rand)

dif = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guess():

    number = int(input("Make a guess : "))
    if rand == number :
        print(f"You got it! The answer was {number}")
        exit()
    elif rand > number : 
        print("go high !! ")
    elif rand < number : 
        print("go low !! ")

def calc(cou):
    counter = 0
    while counter < cou :
        guess()
        cou = cou - 1
        print(f"wrong !!! You have {cou} attempts remaining to guess the number.")
        #number2 = int(input("Make a guess again : "))
        if cou == 0:
            print(f"you lost the value was {rand}")

if dif == "easy":
    cou = 10
    calc(cou)
elif dif == "hard" :
    cou = 5
    calc(cou)
else :
    print("wrong input !! ")
    exit()
