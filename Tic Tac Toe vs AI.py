#Tic Tac Toe vs AI

cpu_opponent = True

cpu_setting = 1
#1 = easy, 2 = medium, 3 = hard, 4 = makes best move possible every round

board = [" " for i in range(10)]
#range 10 instead of 9 to account for 0 index when player is making a move

def printBoard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")

def place_move(symbol, pos):
    board[pos] = symbol

def cpu_move():
    pass

def player_move():
    pass

def plyr_or_cpu():
    opponent_choice = input("Do you wish to play against the CPU? (Y | N)")
    if opponent_choice == "Y" or "y":
        print("You have chosen to play against the CPU.")
        cpu_opponent = True
    elif opponent_choice == "N" or "n":
        print("You have chosen to play againt another player.")
        cpu_opponent = False
    else:
        print("The game did not recognise your input and has defaulted to a CPU opponent.")
    
def cpu_diff():
    cpu_setting_choice = input("Please select a difficuilty setting for the CPU, starting at 1 for Easy, 2 for Medium, 3 for Hard and 4 for Very Hard: ")
    if cpu_setting_choice == 1:
        print("You have selected the Easiest setting for the CPU.")
        cpu_setting = 1
    elif cpu_setting_choice == 2:
        print("You have selected the Medium setting for the CPU.")
        cpu_setting = 2
    elif cpu_setting_choice == 3:
        print("You have selected the Hard setting for the CPU.")
        cpu_setting = 3
    elif cpu_setting == 4:
        print("You have selected the Very Hard setting for the CPU, the CPU will now play the best move possible every round.")
        cpu_setting = 4
    else:
        print("Your input was not recognised and the CPU defaulted to the Easiest Setting.")

def main():
    print("Welcome to my Python Terminal Game of Tic Tac Toe. You can play with another Human or against the CPU!")
    plyr_or_cpu()
    print("Thank you for choosing your opponent!")
    if cpu_opponent == True:
        pass
    elif cpu_opponent == False:
        pass

main()
