def get_row():
    return list("   |   |   ")

def get_bound():
    return list("---+---+---")

def check_for_winner(marker, board):
    '''
    this function checks to see whether three of the same marker, either X or O, are in a row
    parameters:
    marker: str either X or O
    board: 2d list, current state of the board
    returns: True or False
    '''
    # Check all of the vertical lines
    if board[0][1] == marker and board[2][1] == marker and board[4][1] == marker:
        return True
    if board[0][5] == marker and board[2][5] == marker and board[4][5] == marker:
        return True
    if board[0][9] == marker and board[2][9] == marker and board[4][9] == marker:
        return True
    # Check all the horizontal lines
    if board[0][1] == marker and board[0][5] == marker and board[0][9] == marker:
        return True
    if board[2][1] == marker and board[2][5] == marker and board[2][9] == marker:
        return True
    if board[4][1] == marker and board[4][5] == marker and board[4][9] == marker:
        return True
    # Check all the diagonal lines
    if board[0][1] == marker and board[2][5] == marker and board[4][9] == marker:
        return True
    if board[0][9] == marker and board[2][5] == marker and board[4][1] == marker:
        return True
    return False

def main():
    board = [get_row(), get_bound(), get_row(), get_bound(), get_row()]
    player_1 = "X"
    player_2 = "O"
    turn_count = 1
    while True:
        current_player = player_1 if turn_count % 2 == 1 else player_2
        row_pos = input("Choose which row: ")
        col_pos = input("Choose which column: ")

        row_index = 2*int(row_pos)-2

        col_index = 4*int(col_pos)-3
        board[row_index][col_index] = current_player
        for line in board:
            print("".join(line))
        if check_for_winner(current_player, board):
            print("We have a winner!")
            break
        if turn_count == 9:
            print("It's a tie!")
            break
        turn_count += 1
        

if __name__ == '__main__':
    main()