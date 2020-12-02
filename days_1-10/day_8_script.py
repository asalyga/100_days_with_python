import day_8_assets

print(day_8_assets.logo)
print("Welcome to silent auction program.")

game = True
bid_dic = {}


def winner(the_bidding):
    highest_bid = 0
    bid_winner = ""
    for bidder in the_bidding:
        amount = the_bidding[bidder]
        if amount > highest_bid:
            highest_bid = amount
            bid_winner = bidder
    print(f"The winner is {bid_winner} with a bid of ${highest_bid}")


while game:
    player_name = input("What's your name?: ")
    player_bid = int(input("What's your bid?:  $"))
    bid_dic[player_name] = player_bid

    is_anyone = input("Are there any other bidders? (Answer 'yes' or 'no') \n").lower()
    if is_anyone == 'no':
        game = False
        # print(f"The winner is {max(bid_dic, key=bid_dic.get)} with a bid of ${bid_dic[max(bid_dic,
        # key=bid_dic.get)]} " f"\n CONGRATULATIONS")
        print("\n" * 100)
        winner(bid_dic)
    else:
        print("\n"*100)
