#Tic Tac Toe vs AI

#plyr_or_cpu = 0
#needed?


cpu_diff = 0
#0 = easy, 1 = medium, 2 = hard, 3 = makes best move possible every round

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

def makeMove(symbol, pos):
    board[pos] = symbol

def main():
    pass


