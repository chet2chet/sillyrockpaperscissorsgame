import subprocess as sp
import random
# 1 = Rock
# 2 = Paper
# 3 = Scissors

move_list = [1, 2, 3]
cpu_move = random.choice(move_list)

play_again = True
# ROCK PICK
while play_again == True:
    cpu_move = random.choice(move_list)
    try:
        your_move = int(input("Choose your fighter:\n 1/ Rock \n 2/ Paper \n 3/ Scissors \n"))
    except ValueError:
        print("Input a number, you dumbass")

    if your_move == 1 and cpu_move == 1:
        print("Draw")
        play_again = True

    if your_move == 1 and cpu_move == 2:
        print("You lost.")

    if your_move == 1 and cpu_move == 3:
        print("You won.")

    #PAPER PICK
    if your_move == 2 and cpu_move == 1:
        print("You won.")

    if your_move == 2 and cpu_move == 2:
        print("Draw")
        play_again = True

    if your_move == 2 and cpu_move == 3:  
        print("You lost.")      

    #SCISSORS PICK
    if your_move == 3 and cpu_move == 1:
        print("You lost.")

    if your_move == 3 and cpu_move == 2:
        print("You won.")

    if your_move == 3 and cpu_move == 3:  
        print("Draw")
        play_again = True

    play_again = input("Do you want to play again? \n /y \n /n \n")
    if play_again == "y":
        play_again = True
    else:
        exit()
    
    sp.call('clear', shell=True)
