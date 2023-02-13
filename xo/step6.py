board = [1,2,3,4,5,6,7,8,9]
turn = "X" # X, O
winner = ""
is_continue = True

def print_board(board):
    pass

def check_input(value):
    pass

def check_game_is_finished(board):
    pass

def change_turn(turn):
    pass

while is_continue:
    print("===========",turn," turn =============")
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

    # Get input
    n = input("get index:\n")

    try:
        n = int(n)
    except:
        print("=======Nemishe...=======")
        continue

    # Chck input
    if 1<=n<=9 and board[n-1] != "X" and board[n-1] != "O":
        board[n-1] = turn
    else:
        print("\n=======Nemishe...=======")
        continue

    # Check winners
    # vertically - horizontally - x
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
    board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or \
    board[0] == board[4] == board[8] or board[2] == board[4] == board[6] :

       print('============================',turn," is won!!!! ==================")
       winner = True
       is_continue = False

    # Check game is finished or not
    if board[0] != 1 and board[1] != 2 and board[2] != 3 and \
       board[3] != 4 and board[4] != 5 and board[5] != 6 and\
       board[6] != 7 and board[7] != 8 and board[8] != 9:
        is_continue = False

    # Change turn
    if is_continue:
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"
if winner:
    print("========================== ",winner,"won ==========================")
else:
    print("========================== Game is Equal!!!!!!! ==========================")