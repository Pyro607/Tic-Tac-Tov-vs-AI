#Tic Tac Toe vs AI

cpu_setting = 1
#1 = easy, 2 = medium, 3 = hard, 4 = makes best move possible every round

board = [" " for i in range(10)]
#range 10 instead of 9 to account for 0 index when player is making a move

def print_board(board):
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
    keep_running = True
    while keep_running:
        move = input("Input the position you would like to place your X (1 top left - 9 bottom right):")
        

def win_condition(board, symbol):
    return (board[1] == symbol and board[2] == symbol and board[3] == symbol) or
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
    (board[7] == symbol and board[8] == symbol and board[9] == symbol) or
    (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
    (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
    (board[3] == symbol and board[6] == symbol and board[9] == symbol) or
    (board[1] == symbol and board[5] == symbol and board[9] == symbol) or
    (board[3] == symbol and board[5] == symbol and board[7] == symbol)

def is_board_full(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

#def cpu_rand_move():
    #pass

    
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
        print("Your input was not recognised and the CPU defaulted to the previous setting.")

def main():
    print("Welcome to my Python Terminal Game of Tic Tac Toe. You can play against the CPU on varying difficuilty settings!")
    cpu_diff()
    print_board()
    
    while not(is_board_full(board)):
        if not(win_condition(board, "O")):
            player_move()
            print_board()
        else:
            print("Sorry, the CPU outsmarted you...")


        if not(win_condition(board, "X")):
            cpu_move()     
