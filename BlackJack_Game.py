############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("do you want to play the game of BLACK JACK :: y/n  ")



def deal_cards():
    r_cards = random.choice(cards)
    return(r_cards)

def calculate_score(cards): 
    sum = 0
    for i in cards:
        sum += i
    return sum

def compare_score():
    if 


if play == "y":
    user_cards = []
    comp_cards = []

    for i in range(2):
        rand2 = [deal_cards()] # convert the int type of the deal_cards() to list. 
        comp_cards += rand2
    print(f"Dealer's first cards :: {comp_cards[0]}")


    for i in range(2):
        rand = [deal_cards()] # convert the int type of the deal_cards() to list. 
        user_cards += rand 
        '''this += or .extend() will not work because single item cannot be added until its not an list. 
        then in that case the data of deal_cards() needs to be converted to list or use .append() ''' 
    print(f"Your cards :: {user_cards} and the current score is {calculate_score(user_cards)}")

    total_sum = calculate_score(user_cards)
    while total_sum < 21:
        another_pick = input("do you want to pick another card y/n :: ")

        if another_pick == "y":
            rand3 = [deal_cards()]
            user_cards += rand3
            print(user_cards)
            total_sum = calculate_score(user_cards)
            print(f"Total Users Sum :: {total_sum}")
            if total_sum > 21:
                print("you lost and Comp wins")
        
        elif another_pick == "n":



else: 
    exit()



