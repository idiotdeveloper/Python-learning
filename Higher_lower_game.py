import random
import game_data

#print(game_data.data)

def pick_random():

    random_index = random.randrange(len(game_data.data)-1)

    random_dict = game_data.data[random_index]
    print(random_dict)
    random_name = game_data.data[random_index]["name"]
    random_country = game_data.data[random_index]["country"]
    random_description = game_data.data[random_index]["description"]
    random_follower_count = game_data.data[random_index]["follower_count"]
    
    return(random_index, random_name, random_country, random_description,random_follower_count)

def check_input(guess, random_follower_count1, random_follower_count2):

    if guess == "a":
        if random_follower_count1 > random_follower_count2:
            return True
        else:
            return False

    else: 
        if random_follower_count2 > random_follower_count1:
            return True
        else:
            return False

def game(random_follower_count1, random_follower_count2,random_index1,random_name1,random_country1,random_description1, random_index2, random_name2, random_country2, random_description2,score):
    

    guess = input("Who has more followers ? Type 'A' or 'B' :   ").lower()
    
    is_correct = check_input(guess, random_follower_count1, random_follower_count2)

    if is_correct:
        score = score + 1
        print("correct")
        print(f"yout streak :: {score}")
        
        random_index1 = random_index2
        #game_data.data[random_index1] = game_data.data[random_index2]
        #print(game_data.data[random_index1])
        random_name1 = random_name2
        random_country1 = random_country2
        random_description1 = random_description2
        random_follower_count1 = random_follower_count2
        print(f'Compare A :: {game_data.data[random_index1]["name"]}, a {game_data.data[random_index1]["description"]}, from {game_data.data[random_index1]["follower_count"]}') 

        random_index3, random_name3, random_country3, random_description3, random_follower_count3 = pick_random()

        random_index2 = random_index3
        #game_data.data[random_index2] = game_data.data[random_index3]
        #print(game_data.data[random_index2])
        random_name2 = random_name3
        random_country2 = random_country3
        random_description2 = random_description3
        random_follower_count2 = random_follower_count3
        print(f'Compare B :: {game_data.data[random_index2]["name"]}, a {game_data.data[random_index2]["description"]}, from {game_data.data[random_index2]["follower_count"]}') 

        game(random_follower_count1, random_follower_count2,random_index1,random_name1,random_country1,random_description1, random_index2, random_name2, random_country2, random_description2,score)

    else:
        print("wrong")
    
    print(f"yout streak :: {score}")

random_index1, random_name1, random_country1, random_description1, random_follower_count1 = pick_random()    
random_index2, random_name2, random_country2, random_description2, random_follower_count2 = pick_random()

if random_index1 == random_index2:
    random_index2, random_name2, random_country2, random_description2, random_follower_count2 = pick_random()

print(f"Compare A :: {random_name1}, a {random_description1}, from {random_country1}")

print(f"Compare B :: {random_name2}, a {random_description2}, from {random_country2}")

score = 0

game(random_follower_count1, random_follower_count2,random_index1,random_name1,random_country1,random_description1, random_index2, random_name2, random_country2, random_description2, score)

