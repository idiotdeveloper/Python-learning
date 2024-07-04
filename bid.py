bids = {}

def check_highest_bid(bids):  # this function is looping though an dictionary 
    highest_val = 0
    winner_name = ""
    for d in bids:
        if bids[d] > highest_val:
            highest_val = bids[d]
            winner_name = d

    print(f"winnger is : {winner_name} with a bid amount of : {bids[winner_name]}")

cont = False
while not cont :
    name = input("whats your name : ")
    bid_amt = int(input("wnter the bid amount : $"))

    bids[name] = bid_amt
    shd_cont = input("any other users wants to bid : yes/no \n")
    if shd_cont == "no":
        cont = True
        print(bids)
        check_highest_bid(bids)






