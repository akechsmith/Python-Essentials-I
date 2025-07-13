from random import randrange

def display_board(board):
    print("+-------" * 3 + "+")
    for row in range(3):
        print("|       " * 3 + "|")
        for col in range(3):
            print("|   {}   ".format(board[row][col]), end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError("Invalid range")
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ['X', 'O']:
                print("That field is already taken. Try again.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9.")

def make_list_of_free_fields(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['X', 'O']]

def victory_for(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)], # rows
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], # columns
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], # diagonals
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[r][c] == sign for r, c in condition):
            return 'you' if sign == 'O' else 'me'
    return None

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        move = randrange(len(free))
        row, col = free[move]
        board[row][col] = 'X'

# --- Game Engine ---
def main():
    board = [[3 * r + c + 1 for c in range(3)] for r in range(3)]
    board[1][1] = 'X'  # Computer plays first

    human_turn = True
    while True:
        display_board(board)
        if human_turn:
            enter_move(board)
            winner = victory_for(board, 'O')
        else:
            draw_move(board)
            winner = victory_for(board, 'X')

        if winner:
            display_board(board)
            print("You won!" if winner == 'you' else "I won!")
            break

        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break

        human_turn = not human_turn

if __name__ == "__main__":
    main()
