from replit import clear
from art import logo2
#HINT: You can call clear() to clear the output in the console.
print(logo2)
auction = []
othersBidders = ""


def bid_winner(bidding_record):
    greater_bid = 0
    winner = ""
    for key in range(0, len(bidding_record)):

        if bidding_record[key]["bid"] > greater_bid:
            greater_bid = bidding_record[key]["bid"]
            winner = bidding_record[key]["name"]

    print(f"The winner is {winner} with the bid of ${greater_bid}")


while othersBidders != "no":

    name = input("What is your name?:\n")
    while True:
        try:
            bid = float(input("What is your bid?:\n"))
            if bid > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    new_item = {"name": name, "bid": bid}
    auction.append(new_item)

    while True:
        try:
            othersBidders = input(
                "Are there any other bidders? Type 'Yes' or 'No':\n").lower()
            if othersBidders == "yes" or othersBidders == "no":
                break
            else:
                print("Invalid input. Please enter Yes or No.")

        except ValueError:
            print("Invalid input. Please enter Yes or No.")

    if othersBidders == "yes":
        clear()
    else:
        bid_winner(auction)
