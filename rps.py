import random
import os
import time

def clear():
    os.system("clear")

# Now we will set instructions for how the game is played
def rps_instructions():
    print()
    print("Instructions for Rock Paper Scissors : ")
    print()
    print("Rock crushes Scissors!")
    print("Scissors cuts Paper!")
    print("Paper covers Rock!")

def rps():
    global rps_table
    global game_map
    global name

# This is the game loop for each game of Rock Paper Scissors
while True:
    print("-------------------------------------")
    print("\t\tMenu")
    print("-------------------------------------")
    print("Enter \"help\" for instructions")
    print("Enter \"rock\",\"paper\",\"scissors\" to play!")
    print("Enter \"exit\" to quit :(")
    print("-------------------------------------")
    print()

    # Player input HERE
    inp = input("Enter your move! : ")
    if inp.lower() == "help":
        clear()
        rps_instructions()
        continue
    elif inp.lower() == "exit":
        clear()
        break
    elif inp.lower() == "rock":
        player_move = 0
    elif inp.lower() == "paper":
        player_move = 1
    elif inp.lower() == "scissors":
        player_move = 2
    else:
        clear()
        print("Wrong Input!")
        rps_instructions()
        continue
    print("Computer making move...")
    print()
    time.sleep(2)

    # Randomly choose computer's move
    comp_move = random.randint(0,2)

    # Print computer's move
    print("Computer chooses ", game_map[comp_move].upper())

    # Determine winner of the match
    winner = rps_table[player_move][comp_move]

    # Declare the winner of the game
    if winner == player_move:
        print(name, "WINS!!!")
    elif winner == comp_move:
        print("COMPUTER WINS!!!")
    else:
        print("TIE GAME!!!")
    print()
    time.sleep(2)
    clear()




# This is what will be mapped between moves and numbers
game_map = {0:"rock", 1:"paper", 2:"scissors"}

# This is the win-lose matrix that will determine the winner
rps_table = [[-1,1,0], [1,-1,2], [0,2,-1]]

name = input("Enter your name")

# Creating the game loop
while True:
    
    # This is the game menu
    print()
    print("Let's Play some Rock Paper Scissors!")
    print("Enter 1 to play Rock Paper Scissors")
    print("Enter 2 to quit")
    print()

    try:
        choice = int(input("Enter your choise = "))
    except ValueError:
        clear()
        print("Wrong Choice")
        continue

    # Play game
    if choice == 1:
    # Quit game loop
    elif choice == 2:
        break
    # Wrong input
    else:
        clear()
        print("That is the wrong choice. Please read instructions again")
