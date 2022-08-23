row = list("   |   |   ")
boundary = list("---+---+---")

board = [row, boundary, row, boundary, row]
player_1 = "X"
player_2 = "O"
row_pos = input("Choose which row: ")
col_pos = input("Choose which column: ")

row_index = 2*int(row_pos)-2

col_index = 4*int(col_pos)-3
board[row_index][col_index] = player_1
for line in board:
    print("".join(line))