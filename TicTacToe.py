WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6),             # Diagonals
]

HUMAN = "X"
AI = "O"


def print_board(board):
    """Display the board, using numbers for empty squares."""
    cells = [
        board[i] if board[i] != " " else str(i + 1)
        for i in range(9)
    ]

    print(f"\n {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}\n")


def get_winner(board):
    """Return the winning symbol, or None if nobody has won."""
    for a, b, c in WINNING_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def minimax(board, is_ai_turn):
    """
    Return the best score for the current position.

    AI win: +1
    Human win: -1
    Draw: 0
    """
    winner = get_winner(board)

    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if " " not in board:
        return 0

    if is_ai_turn:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def get_ai_move(board):
    """Choose the empty square with the best Minimax score."""
    best_score = float("-inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def play_game():
    board = [" "] * 9
    print("Tic-Tac-Toe: You are X, the AI is O.")
    print("Choose a square by entering a number from 1 to 9.")

    while True:
        print_board(board)

        # Human's turn
        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    print("That square is unavailable. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a number from 1 to 9.")

        board[move] = HUMAN

        if get_winner(board) == HUMAN:
            print_board(board)
            print("You win!")
            return
        if " " not in board:
            print_board(board)
            print("It's a draw!")
            return

        # AI's turn
        ai_move = get_ai_move(board)
        board[ai_move] = AI
        print(f"The AI chooses square {ai_move + 1}.")

        if get_winner(board) == AI:
            print_board(board)
            print("The AI wins!")
            return
        if " " not in board:
            print_board(board)
            print("It's a draw!")
            return


if __name__ == "__main__":
    play_game()
