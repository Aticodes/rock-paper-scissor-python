import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


playerchoice = input("select \n 1 for Rock, \n 2 for Paper or \n 3 for Scissor : \n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("please only select the given numbers 1, 2 or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose : " + str(RPS(player)).replace('RPS.','') + ".")
print("Python chose : " + str(RPS(computer)).replace('RPS.','') + ".\n")

if player == 1 and computer == 3:
    print("🎉you win!")
elif player == 2 and computer == 1:
    print("🎉you win!")
elif player == 3 and computer == 2:
    print("🎉you win!")
elif player == computer:
    print("😲Its a Tie!")
else:
    print("🐍python wins!")