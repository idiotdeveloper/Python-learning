target = int(input("enter the range :: "))

total = 0

for i in range(1, target+1):
    if i%2 == 0:
        total += i
    
print(total)
