#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
myletters = str()
mysymbols = str()
mynumbers = str()

for index in range(0, nr_letters):
    randomLetter = str(random.choice(letters))
    myletters = myletters + randomLetter

for index2 in range(0, nr_symbols):
    randomSymbol = str(random.choice(symbols))
    mysymbols = mysymbols + randomSymbol

for index3 in range(0, nr_numbers):
    randomNumber = str(random.choice(numbers))
    mynumbers = mynumbers + randomNumber

myPassword = myletters + mysymbols + mynumbers

print(myPassword)
'''

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

myPasswordRandom = []
randomisedPassword = str()
for index in range(0, nr_letters):

  myPasswordRandom.append(str(random.choice(letters)))

for index2 in range(0, nr_symbols):

  myPasswordRandom.append(str(random.choice(symbols)))

for index3 in range(0, nr_numbers):

  myPasswordRandom.append(str(random.choice(numbers)))

random.shuffle(myPasswordRandom)

for index4 in range(0, len(myPasswordRandom)):
  myPassword2 = str(myPasswordRandom[index4])
  randomisedPassword = randomisedPassword + myPassword2

print(randomisedPassword)
