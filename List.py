import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

number_of_names = len(names)
print(number_of_names)

print(names)

counter = 0
for i in names:
    counter += 1
print(counter)

choose = random.randint(0, counter-1)

print(f"{names[choose]} is going to buy the meal today!")