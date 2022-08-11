board = []

for i in range(3):
    row = []
    for j in range(3):
        row.append("-")
    board.append(row)

board[0][2] = "X"
board[1][1] = "X"
board[2][0] = "X"

print(len(board))

for i in range(3):
    print("i:" + str(i))
    print("what:" + str(3 - 1 - i))
    print(board[i][3 - 1 - i])
    if board[i][3 - 1 - i] != "X":
        print("NO")



print("Seems fine?")
