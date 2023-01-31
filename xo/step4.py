board = [1,2,3,4,5,6,7,8,9]
turn = "X" # X, O

while True:
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

    # Check winner
    # vertically - horizontally - x
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
    board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or \
    board[0] == board[4] == board[8] or board[2] == board[4] == board[6] :

       print('============================',turn," is won!!!! ==================")
       break
    else:
        is_finished = False
        for i in range(9):
            if board[i] == str(i+1):
                is_finished = True
        if is_finished == True:
            break

    # Change turn
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"