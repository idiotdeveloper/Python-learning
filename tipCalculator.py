print("Welcome to Tip and Split Calculator\n")

amt = input("what is the total bill amount\n")
f_amt = float(amt)

tip_perc = input("what is the tip percentage you want to add ? 0, 5, 10, 15, 20 or any amount you like?\n")

tip_amt = f_amt * (float(tip_perc)/100)

print(f"Total Tip amount = {tip_amt}")

total_amt = tip_amt + f_amt
print(f"Total amount = {total_amt}")

split = input("how many peoples\n")
i_split = int(split)

split_amt = total_amt / i_split
round_split = round(split_amt, 2)

print(f"Each person should pay = {round_split}")




