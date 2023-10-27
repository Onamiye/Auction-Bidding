Auction = {}
person_bidding = ""
def find_highest_bidder(Auction):
  highest_bid = 0
  for bidder in Auction:
    bid_amount = Auction[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      person_bidding = bidder



  print(f"The winner is {person_bidding} with ${highest_bid}")


done = False
while not done:
  Name = input("What is your name?: ")
  Bid = int(input("How much are you willing to bid?: $"))
  Auction[Name] = Bid
  Other_players = input("Are there any other bidders? Please type 'yes' or 'no': ").lower()
  if Other_players == "no":
    done = True
    find_highest_bidder(Auction)
  else:
    done = False
