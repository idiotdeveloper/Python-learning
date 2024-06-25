height = input("height")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("weight")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

fh = float(height)
pow = fh**2
print("h :: " + str(pow))

bmi = (float(weight)/pow)
print(int(bmi))