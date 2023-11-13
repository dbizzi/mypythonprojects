rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

playerChoice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"
    ))
if playerChoice >= 3 or playerChoice < 0:
  print("You typed a invalid Number, You Lose")
else:
  optionsList = [rock, paper, scissors]

  playerOption = optionsList[playerChoice]

  randomCPUChoice = random.randint(0, 2)

  cpuOption = optionsList[randomCPUChoice]

  print(optionsList[playerChoice])
  print("Computer Chose")
  print(optionsList[randomCPUChoice])

  if playerChoice == 0 and randomCPUChoice == 2:
    print("You win")
  elif playerChoice == 2 and randomCPUChoice == 1:
    print("You win")
  elif playerChoice == 1 and randomCPUChoice == 0:
    print("You win")
  elif playerChoice == randomCPUChoice:
    print("You draw")
  elif randomCPUChoice > playerChoice:
    print("You lose")
  elif randomCPUChoice == 0 and playerChoice == 2:
    print("You lose")
  else:
    print("You lose")
