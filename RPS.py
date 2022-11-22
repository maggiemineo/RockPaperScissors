# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''ROCK 
    ______
---'   ___)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''SCISSORS
    ___
---'   )_______
  (      _______)
       __________)
      (___)
---.__(__)
'''

#Write your code below this line 👇
import random

options=[rock,paper,scissors]
win = 0

numgames = int(input("How many games do you want to play?"))
games= list(range(numgames))

for x in games:
 #Start games
  yourChoice = int(input("What do you Choose? type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
  
  if yourChoice > 2:
    print("You typed an invalid number, must be a valid choice: 0 for Rock, 1 for paper or 2 for Scissors !")
    games.append(max(games)+1)
  else:
    print(options[yourChoice])
    pcChoice = random.randint(0,2)
    print("Computer chose:")
    print(options[pcChoice])
    if yourChoice == pcChoice:
        print("Its a Tie")
    elif yourChoice == 0 and pcChoice == 1:
        print("You Lose!")
    elif yourChoice == 1 and pcChoice == 2:
        print("You Lose!")
    elif yourChoice == 2 and pcChoice == 0:
        print("You Lose!")
    else:
        print("You Win!")
        win +=1

print(f"\nYou won {win} out of {numgames} games!")

winRate=round((win/numgames) * 100,2)

print(f"\nThats a {winRate}% Win Rating\n")

if winRate >75:
  print("You are a BEAST!")
elif winRate >45:
  print("That was not to shabby!")
elif winRate >25:
  print("At least you showed up!") 
else:  
  print("What the HECKOLA was That!")