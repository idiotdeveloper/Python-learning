line1 = ["a1","b1","c1"]
line2 = ["a2","b2","c2"]
line3 = ["a3","b3","c3"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


for i in map:
    counter2 = 0
    for y in i:
        counter2 += 1
        if position == y:
            print("matched :", position, y, counter2)
            i[counter2-1] = "X"
            print(i)
        print(y)
   

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")