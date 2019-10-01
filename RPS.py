# Teylon Pace 
# Rock Paper Scissors Game
#______________________________________________________________________
# break into pieces
# Welcome page, with name entry
# Score screen with Computer, player (name), ties
# Options for game r, p, s, q
# Game will loop until q is entered
# Each loop it will get a random choice from the computer
# a choice from the player, compare the two, and update the score
# When the game is over (q is entered) final score will be displayed
#______________________________________________________________________

# Imports
import random
# Variables
playerScore = 0
computerScore = 0
ties = 0
# make a list
cChoices =["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter in your name ")
# main loop
while True:
	# Print score
	print("Score:")
	print("Computer: " + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, 'q' to quit: ")
	computerChoice = random.choice(cChoices)
	print(computerChoice)
	if choice == "q":
		break

	if choice == "r":
		print(name + " Picked Rock")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")
			computerScore += 1
		else:
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore += 1 
	elif choice  == "p":
		print(name + " Picked Paper")
		if computerChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "s":
			print("Computer picked Scissors")
			print("Scissors beats Paper")
			computerScore += 1
		else:
			print("Computer picked Rock")
			print("Paper beats Rock")
			playerScore += 1 
	elif choice == "s": 
		print(name + " Picked Scissors")
		if computerChoice == "s":
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore += 1
		else:
			print("Computer picked Paper")
			print("Scissors beats Paper")
			playerScore += 1 
	else:
		print("Invalid entry, please try again")


