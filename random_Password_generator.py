import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

list = []

for i in letters:
    char = random.choices(letters, weights = None, k = nr_letters)
print(char)
list = list + char
print(list)

for i in numbers:
    num = random.choices(numbers, weights = None, k = nr_numbers)
print(num)
list = list + num
print(list)


for i in symbols:
    sym = random.choices(symbols, weights = None, k = nr_symbols)
print(sym)
list = list + sym
print(list)

random.shuffle(list)
print(list)

str = ""

for el in list:
    str += el

print(f"you random password ::  {str}")