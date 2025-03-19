square_board = []
for i in range(3):
    row = input().split()
    square_board.append(row)

# Check if 'O' wins
is_there_o_in_row = (
    # Horizontal wins
    (square_board[0][0] == "O" and square_board[0][1] == "O" and square_board[0][2] == "O") or
    (square_board[1][0] == "O" and square_board[1][1] == "O" and square_board[1][2] == "O") or
    (square_board[2][0] == "O" and square_board[2][1] == "O" and square_board[2][2] == "O") or
    
    # Vertical wins
    (square_board[0][0] == "O" and square_board[1][0] == "O" and square_board[2][0] == "O") or
    (square_board[0][1] == "O" and square_board[1][1] == "O" and square_board[2][1] == "O") or
    (square_board[0][2] == "O" and square_board[1][2] == "O" and square_board[2][2] == "O") or
    
    # Diagonal wins
    (square_board[0][0] == "O" and square_board[1][1] == "O" and square_board[2][2] == "O") or
    (square_board[0][2] == "O" and square_board[1][1] == "O" and square_board[2][0] == "O")
)

# Check if 'X' wins
is_there_x_in_row = (
    # Horizontal wins
    (square_board[0][0] == "X" and square_board[0][1] == "X" and square_board[0][2] == "X") or
    (square_board[1][0] == "X" and square_board[1][1] == "X" and square_board[1][2] == "X") or
    (square_board[2][0] == "X" and square_board[2][1] == "X" and square_board[2][2] == "X") or
    
    # Vertical wins
    (square_board[0][0] == "X" and square_board[1][0] == "X" and square_board[2][0] == "X") or
    (square_board[0][1] == "X" and square_board[1][1] == "X" and square_board[2][1] == "X") or
    (square_board[0][2] == "X" and square_board[1][2] == "X" and square_board[2][2] == "X") or
    
    # Diagonal wins
    (square_board[0][0] == "X" and square_board[1][1] == "X" and square_board[2][2] == "X") or
    (square_board[0][2] == "X" and square_board[1][1] == "X" and square_board[2][0] == "X")
)

# Output the result
if is_there_o_in_row:
    print("Abhinav Wins")
elif is_there_x_in_row:
    print("Anjali Wins")
else:
    print("Tie")