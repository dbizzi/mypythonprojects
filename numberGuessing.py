from random import randrange
from art import logo4

NUMBER = randrange(1, 100, 1)
EASY_LEVEL = 10
HARD_LEVEL = 5


def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL


def guess_number():
    guess = int(input("Make a guess: "))
    if guess < NUMBER:
        return "Too low"

    elif guess > NUMBER:
        return "Too high"

    else:
        print(f"You got it! The answer was {NUMBER}")
        return 0


print(logo4)

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100")

attemps = difficulty()

while attemps != 0:
    print(f"You have {attemps} attempts remaining to guess the number")
    result = guess_number()
    if result == 0:
        attemps = result
    else:
        print(result)
        attemps -= 1
        if attemps == 0:
            print("You lose")
        else:
            print("Guess again")
