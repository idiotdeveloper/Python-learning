all_score = input("enter all numbers with a space in between :: 10 20 30 40  .. .. .. .. \n")
all_score = all_score.split()

print(all_score)

for i in range(0, len(all_score)):
    all_score[i] = int(all_score[i])
print(all_score)

highest_score = 0

for i in all_score:
    print (i)
    if i > highest_score:
        highest_score = i

print(f"The highest score in the class is: {highest_score}")

