#Tic Tac Toe vs AI

cpu_setting = 1
#1 = easy, 2 = medium, 3 = hard, best move possible every round

board = [" " for i in range(10)]
#range 10 instead of 9 to account for 0 index when player is making a move

last_player_move = 0
#records what the last move made by the player was, important for allowing the AI to make the best possible move

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

def pos_is_free(y):
    return board[y] == " "

#What cpu difficuilty setting? will determine how moves are calculated
# - Hard Setting :
# 1. winning move
# 2. block winning player move
# 3. if player went in corner, go in center
# 4. if player went in center, go in corner
# 5. if player wen on edge, go in center
# 6. go on edge
# 7. only 1 place left
# 8. no space left

# - Medium Setting:
# 1. Places in a random position every round

# - Easy Setting:
# 1. Places in a position that will maximise the player's chance of winning, cpu plays a terrible move
def cpu_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0 #default value that can be checked later in main()
    if cpu_setting = 3:
        for letter in ["O", "X"]:
            for i in possible_moves:
                board_copy = board[:]
                board_copy[i] = letter
                if win_condition(board_copy, letter)
                    move = i
                    return move #step 1 and 2
        if 
            
    elif cpu_setting = 2:
        pass
    elif cpu_setting = 1:
        pass


def record_last_player_move():
    pass

def player_move():
    keep_running = True
    while keep_running:
        move = input("Input the position you would like to place your X (1 top left - 9 bottom right):")
        try:
            if move > 0 and move < 10:
                if pos_is_free(y):
                    keep_running = False
                    place_move("X", move)
                else:
                    print("This space is invalid, please enter another shortly!")
            else:
                print("Please input a number between 1 and 9 that is not occupied to make your move.")
        except:
            print("Please input another position.")
  

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
    cpu_setting_choice = input("Please select a difficuilty setting for the CPU, starting at 1 for Easy, 2 for Medium, 3 for Hard: ")
    if cpu_setting_choice == 1:
        print("You have selected the Easiest setting for the CPU.")
        cpu_setting = 1
    elif cpu_setting_choice == 2:
        print("You have selected the Medium setting for the CPU.")
        cpu_setting = 2
    elif cpu_setting_choice == 3:
        print("You have selected the Hard setting for the CPU, the CPU will now play the best move possible every round.")
        cpu_setting = 3
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
            break


        if not(win_condition(board, "X")):
            move = cpu_move()     




















