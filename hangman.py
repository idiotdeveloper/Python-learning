import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


print("guess the animal name")
random_word_list = ["lion", "elephant", "tiger", "rabbit", "deer", "monkey", "bear", "fox", "dog", "cat", "zebra"]

chosen_word = random.choice(random_word_list)
print(chosen_word)

create_list = len(chosen_word)
print (create_list)

#creating a empty list and adding space to it. the number of spaces will be equal to the length of the randomly chosen word. 

list_new = []
for i in range(create_list):
    list_new = list_new + [" "]
print(list_new)


# from here the user guess is starting

end_game = False
life = 6

# while loop to itterate till the game ends and here the end requiremens are either 6 lives or all correct. 

while not end_game:

    guess = input("guess the first word :: ").lower()
    guess = guess[0]
    print(guess)

    counter = 0 # this counter is used to track the position of the guessed letter if found in the chosen word. 
    
    # for loop to itterate though all the characeters in the chosen word from the list for animal names

    for i in chosen_word:   
        
        if guess == i:
            print("letter matches")
            list_new[counter] = i #if the guessed letter is found in the chosen word then the value of that position in the list = list_new in replaced by the current value of i. 
        else:
            print("letter did not match")

        counter += 1 #at every itteration the counter value is increased to get the currect posion of the guessed letter where found in the chosen word

    print(list_new)

    # checking if the gussed word does not match then decrease the life by 1 and print the asccii 
    if guess not in chosen_word:
        life -= 1
        #print (life)
        print(stages[life])
        print(f"you have total {life} lives : 1 mistake 1 life")
        if life == 0 :
            end_game = True
            print ("end of game and you lose")
            
    # checking if the gussed word match and there is no space left in the list created with all spaces then end the game with a win 

    if " " not in list_new:
        print("End of Game and you win")
        end_game = True


