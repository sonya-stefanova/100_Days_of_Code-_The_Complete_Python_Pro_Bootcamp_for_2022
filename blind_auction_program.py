from blind_auction_logo import logo
print(logo)
bids = {}
bidding_end = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for curr_bidder in bidding_record:
        bid_amount = bidding_record[curr_bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = curr_bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")


while not bidding_end:
    name = input("What is your name? \n")
    price = int(input("What is your price offer? $"))
    bids[name] = price
    restart = input("Are there are any other bidders? Please, type 'yes' or 'no' \n")
    if restart == "no":
        bidding_end = True
        find_highest_bidder(bidding_record=bids)
        print(f"Thanks for your participation!")