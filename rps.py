from random import randint

options = ["Rock", "Paper", "Scissors"]
Player_Score = 0
Bot_Score = 0
bot = options[randint(0,2)]

play_1 = input("Would you like to play Rock, Paper, Scissors? ")
if play_1 == "Yes":
        player = False
else:
	player = True

while player == False:
	player = input("Rock, Paper, Scissors? ")
	if player == bot:
		print("Tie. Nobody Wins.")
	elif player == "Rock":
		if bot == "Paper":
			print("You Lose. Paper Beats Rock.")
			Bot_Score = Bot_Score + 1
		else:
			print("You Win! Rock Beats Scissors.")
			Player_Score = Player_Score + 1
	elif player == "Paper":
		if bot == "Scissors":
			print("You Lose. Scissors Beats Paper.")
			Bot_Score = Bot_Score + 1
		else:
			print("You Win! Paper Beats Rock.")
			Player_Score = Player_Score + 1
	elif player == "Scissors":
		if bot == "Rock":
			print("You Lose. Rock Beats Scissors.")
			Bot_Score = Bot_Score + 1
		else:
			print("You Win! Scissors Beats Paper.")
			Player_Score = Player_Score + 1
	else:
		print("Invalid Input")
		
	play_2 = input("Would you like to play again? ")
	if play_2 == "Yes":
		bot = options[randint(0,2)]
		player = False
	else:
		player = True

print("Your Score Was",Player_Score,". The Bot's Score Was",Bot_Score,".")
