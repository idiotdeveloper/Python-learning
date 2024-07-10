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

def deal_cards():
    r_cards = random.choice(cards)
    return(r_cards)


def calculate_score(cards): 

    if  sum(cards) >=21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    sum1 = 0
    for i in cards:
        sum1 += i
    return sum1


def compare_result(total_sum,total_comp_sum):

    if total_comp_sum == 0:
        print(f"comp wins!!")
        
    elif total_sum == 0:
        print(f"you won !!")
        
    elif total_sum > 21:
        print("You lost and Computer wins!!")
        
    elif total_comp_sum > 21:
        print("You Win and Computer lost!!")
      
    elif total_comp_sum > total_sum and total_comp_sum <= 21:
        print(f"COMP Wins {total_comp_sum}!!")     
        
    elif total_sum == total_comp_sum:
        print(f"It's a DRAW !!!!!")
        
    else:
        print(f"User Wins {total_sum}!!")
    

def game():  

    
    user_cards = []
    comp_cards = []

    for i in range(2):
        rand2 = [deal_cards()] # convert the int type of the deal_cards() to list. 
        comp_cards += rand2
    print(f"Dealer's first cards :: {comp_cards} and the current score is {calculate_score(comp_cards)} ")


    for i in range(2):
        rand = [deal_cards()] # convert the int type of the deal_cards() to list. 
        user_cards += rand 
        '''this += or .extend() will not work because single item cannot be added until its not an list. 
        then in that case the data of deal_cards() needs to be converted to list or use .append() ''' 
    print(f"Your cards :: {user_cards} and the current score is {calculate_score(user_cards)}")

    total_sum = calculate_score(user_cards)
    total_comp_sum = calculate_score(comp_cards)
    
    pick_another_card = False


    while not pick_another_card:
        another_pick = input("Do you want to pick another card y/n :: ")

        if another_pick == "y":
            rand3 = [deal_cards()]
            user_cards += rand3
            print(user_cards)
            total_sum = calculate_score(user_cards)
            print(f"Total Users Sum :: {total_sum}") 
            if (total_sum > 21):
                pick_another_card = True

        else:
            pick_another_card = True

    while total_comp_sum !=0 and total_comp_sum < 17 and total_sum <= 21:
        #another_pick = input("Do you want to pick another card y/n :: ")
        
        rand3 = [deal_cards()]
        comp_cards += rand3
        print(comp_cards)
        total_comp_sum = calculate_score(comp_cards)
        print(f"Total Comp Sum :: {total_comp_sum}")

    print(f"user Cards :: {user_cards} and the total Sum is :: {total_sum}")
    print(f"Comp Cards :: {comp_cards} and the total Sum is :: {total_comp_sum}")  
    compare_result(total_sum,total_comp_sum)
    


while input("do you want to play the game of BLACK JACK :: y/n  ") == "y":
    game()
