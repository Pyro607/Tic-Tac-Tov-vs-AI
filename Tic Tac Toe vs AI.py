#Tic Tac Toe vs AI

cpu_setting = 2
#1 = easy, 2 = medium, 3 = hard, best move possible every round

board = [" " for i in range(10)]
#range 10 instead of 9 to account for 0 index when player is making a move

last_player_move = 0
#records what the last move made by the player was, important for allowing the AI to make the best possible move

def print_board(board):
    print("1  |2  |3")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("4  |5  |6")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("7  |8  |9")
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
# 5. if player went on edge, go in center
# 5.5 if you go in an edge, the bot goes center, if you then go in an adjacent edge, the bot will go in an edge, you can then fill in the corner between the 2 edges you went in and get a guarnateed win
# 5.5.5 go on a corner if available
# 6. go on edge
# 7. pick a random spot of any spots left
# 8. no space left

# - Medium Setting:
# 1. Places in a random position every round

# - Easy Setting:
# 1. Reverse Hard Setting (Step 8 will still come last)
def cpu_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0 #default value that can be checked later in main()
    corner_moves = [1, 3, 7, 9]
    edge_moves = [2, 4, 6, 8]
    center_move = [5]
    if cpu_setting == 3:
        for letter in ["O", "X"]:
            for i in possible_moves:
                board_copy = board[:]
                board_copy[i] = letter
                if win_condition(board_copy, letter):
                    move = i
                    return move #step 1 and 2

        if last_player_move in [1, 3, 7, 9]:
            if 5 in possible_moves:
                move = 5
                return move #step 3
            
        if last_player_move == 5:
            open_corners1 = []
            for y in possible_moves:
                if y in [1, 3, 7, 9]:
                    open_corners1.append(y)
            if len(open_corners1) > 0:
                move = select_random(open_corners1)
                return move #step 4

        if last_player_move in [2, 4, 6, 8]:
            if 5 in possible_moves:
                move = 5
                return move #step 5

        if (board[2] == "X" and board [4] == "X"):
            if 1 in possible_moves:
                move = 1
                return move #step 5.5

        if (board[4] == "X" and board [8] == "X"):
            if 7 in possible_moves:
                move = 7
                return move #step 5.5

        if (board[8] == "X" and board [6] == "X"):
            if 9 in possible_moves:
                move = 9
                return move #step 5.5

        if (board[6] == "X" and board [2] == "X"):
            if 3 in possible_moves:
                move = 3
                return move #step 5.5

        open_corners3 = []
        for q in possible_moves:
            if q in [1, 3, 7, 9]:
                open_corners3.append(q)
        if len(open_corners3) > 0:
            move = select_random(open_corners3)
            return move #step 5.5.5

        open_edges1 = []
        for y in possible_moves:
            if y in [2, 4, 6, 8]:
                open_edges1.append(y)
        if len(open_edges1) > 0:
            move = select_random(open_edges1)
            return move #step 6

        if len(possible_moves) > 0:
            move = select_random(open_corners1)
            return move #step 7

        return move #step 8

    elif cpu_setting == 2:
        if len(possible_moves) > 0:
            move = select_random(possible_moves)
            return move
        else:
            return move

    elif cpu_setting == 1:
        open_edges2 = []
        for y in possible_moves:
            if y in [2, 4, 6, 8]:
                open_edges2.append(y)
        if len(open_edges2) > 0:
            move = select_random(open_edges2)
            return move #step 6 (and 7 essentially) REVERSED for easy difficuilty

        if last_player_move in [2, 4, 6, 8]:
            if 5 in possible_moves:
                move = 5
                return move #step 5 REVERSED for easy difficuilty

        if last_player_move == 5:
            open_corners2 = []
            for y in possible_moves:
                if y in [1, 3, 7, 9]:
                    open_corners2.append(y)
            if len(open_corners2) > 0:
                move = select_random(open_corners2)
                return move #step 4 REVERSED for easy difficuilty

        if last_player_move in [1, 3, 7, 9]:
            if 5 in possible_moves:
                move = 5
                return move #step 3 REVERSED for easy difficuilty

        for letter in ["O", "X"]:
            for i in possible_moves:
                board_copy = board[:]
                board_copy[i] = letter
                if win_condition(board_copy, letter):
                    move = i
                    return move #step 1 and 2 REVERSED for easy difficuilty

        if len(possible_moves) > 0:
            move = select_random(open_corners1)
            return move #step 7

        return move #step 8 
    

def select_random(list):
    import random
    length = len(list)
    r = random.randrange(0, length)
    return list[r]
    

def player_move():
    global last_player_move
    keep_running = True
    while keep_running:
        move = input("Input the position you would like to place your X (1 top left - 9 bottom right):")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if pos_is_free(move):
                    keep_running = False
                    place_move("X", move)
                    last_player_move = move
                else:
                    print("This space is invalid, please enter another shortly!")
            else:
                print("Please input a number between 1 and 9 that is not occupied to make your move.")
        except:
            print("Please input another position.")
  

def win_condition(board, symbol):
    return (board[1] == symbol and board[2] == symbol and board[3] == symbol) or (board[4] == symbol and board[5] == symbol and board[6] == symbol) or (board[7] == symbol and board[8] == symbol and board[9] == symbol) or (board[1] == symbol and board[4] == symbol and board[7] == symbol) or (board[2] == symbol and board[5] == symbol and board[8] == symbol) or (board[3] == symbol and board[6] == symbol and board[9] == symbol) or (board[1] == symbol and board[5] == symbol and board[9] == symbol) or (board[3] == symbol and board[5] == symbol and board[7] == symbol)

def is_board_full(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

    
def cpu_diff():
    global cpu_setting
    cpu_setting_choice = input("Please select a difficuilty setting for the CPU, starting at 1 for Easy, 2 for Medium, 3 for Hard: ")
    cpu_setting_choice = int(cpu_setting_choice)
    if cpu_setting_choice == 1:
        print("You have selected the Easiest setting for the CPU.")
        cpu_setting = 1
    elif cpu_setting_choice == 2:
        print("You have selected the Medium setting for the CPU.")
        cpu_setting = 2
    elif cpu_setting_choice == 3:
        print("You have selected the Hard setting for the CPU.")
        cpu_setting = 3
    else:
        print("Your input was not recognised and the CPU defaulted to the medium setting.")

def main():
    print("Welcome to my Python Terminal Game of Tic Tac Toe. You can play against the CPU on varying difficuilty settings!")
    cpu_diff()
    print_board(board)
    
    while not(is_board_full(board)):
        if not(win_condition(board, "O")):
            player_move()
            print_board(board)
        else:
            print("Sorry, the CPU outsmarted you...")
            break


        if not(win_condition(board, "X")):
            move = cpu_move()
            if move == 0:
                print("The game has tied, neither playerer has won.")
            else:
                place_move("O", move)
                print("The Computer has made its move, now it's your turn.")
                print_board(board)
        else:
            print("You have won the match!")
            break
main()










