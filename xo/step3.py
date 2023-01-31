board = [1,2,3,4,5,6,7,8,9]

while True:
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

    n = input("get index:\n")

    try:
        n = int(n)
    except:
        print("=======Nemishe...=======")
        continue

    if 1<=n<=9 and board[n-1] == "X":
        print("\n=======Nemishe...\=======n")
    else:
        board[n-1] = "X"