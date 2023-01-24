board = [1,2,3,4,5,6,7,8,9]

print(board[0],board[1],board[2])
print(board[3],board[4],board[5])
print(board[6],board[7],board[8])

n = int(input("get index:\n"))

board[n-1] = "X"

print(board[0],board[1],board[2])
print(board[3],board[4],board[5])
print(board[6],board[7],board[8])

n = int(input("get index:\n"))

if board[n-1] == "X":
    print("Nemishe...\n")
else:
    board[n-1] = "X"

print(board[0],board[1],board[2])
print(board[3],board[4],board[5])
print(board[6],board[7],board[8])

n = int(input("get index:\n"))

if board[n-1] == "X":
    print("Nemishe...\n")
else:
    board[n-1] = "X"

print(board[0],board[1],board[2])
print(board[3],board[4],board[5])
print(board[6],board[7],board[8])
