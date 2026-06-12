# Tic Tac Toe Game
# Write code for tic tac toe game in python. 
# The game should be played between two players, X and O. 
# The game should be played on a 3x3 grid. 
# The players take turns placing their marks (X or O) on the grid. 
# The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game. 
# If all nine squares are filled and neither player has three in a row, the game is a draw. 
# The game should be played in the console, and the players should be able to input their moves by specifying the row and column where they want to place their mark.
# Here's a simple implementation of a tic tac toe game in Python:

def print_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
    print()


def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move as row and column (1-3 separated by a space): ")
            row, col = map(int, move.strip().split())
            if row not in {1, 2, 3} or col not in {1, 2, 3}:
                print("Please enter numbers between 1 and 3 for both row and column.")
                continue
            if board[row - 1][col - 1] != " ":
                print("That square is already taken. Choose another one.")
                continue
            return row - 1, col - 1
        except ValueError:
            print("Invalid input. Enter two numbers separated by a space, for example: 2 3")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins! Congratulations!")
            break
        if check_draw(board):
            print("The game is a draw.")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
