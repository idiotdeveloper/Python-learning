import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = int(input("What do you choose? 0 for Rock, 1 for paper, 2 for scissors :: "))

if choose == 0:
    print(rock)

elif choose == 1:
    print(paper)

elif choose == 2:
    print(scissors)

else: 
    print("wrong input")
    exit()

comp = random.randint(0,2)

print(f"Computer Choose :: {comp}")

if comp == 0:
    print(rock)

elif comp == 1:
    print(paper)

else:
    print(scissors)


if (comp == choose):
    print("draw")

elif ((comp == 0 and choose == 2) or (comp == 2 and choose == 1) or (comp == 1 and choose == 0)): 
    print("Comp Wins")

else:
    print("You win")

