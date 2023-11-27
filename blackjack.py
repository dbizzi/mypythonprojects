import random
from art import logo3
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    score = sum(list_of_cards)
    if score == 21 and len(list_of_cards) == 2:
        return 0
    elif score > 21 and list_of_cards[-1] == 11:
        list_of_cards[-1] = 1
        return score
    return score


def compare(p_score, d_score):
    if p_score == d_score:
        return "Draw"
    elif d_score == 0:
        return "You lose, opponent has Blackjack"
    elif p_score == 0:
        return "You win with a Blackjack"
    elif p_score > 21:
        return "You went over 21, You lose"
    elif d_score > 21:
        return "Dealer went over 21, You win"
    elif p_score > d_score:
        return "You win"
    else:
        return "You lose"


def game_logic():
    print(logo3)
    player = []
    dealer = []
    game_over = False
    for _ in range(2):
        player.append(deal_card())
        dealer.append(deal_card())

    while not game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)
        print(f"Your cards:{player}, current score: {player_score} ")
        print(f"Computer first card: {dealer[0]} ")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                player.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer.append(deal_card())
        dealer_score = calculate_score(dealer)

    print(f"Your final cards:{player}, final score: {player_score} ")
    print(f"Dealer final cards: {dealer}, final score: {dealer_score} ")
    print(compare(player_score, dealer_score))


while input(
        "Do you wanna play a Blackjack game? Type 'y or 'n': ").lower() == "y":
    clear()
    game_logic()
