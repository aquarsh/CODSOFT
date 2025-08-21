import math

def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row*3:(row+1)*3]))
        if row < 2:
            print("---------")
    print("\n")

def check_winner(board):
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Draw"
    return None

def minimax(board, is_maximizing):
    result = check_winner(board)
    if result == "O": return 1
    if result == "X": return -1
    if result == "Draw": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def play_game():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe! 🤖")
    print("You are X, AI is O")
    print_board(board)

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("❌ Invalid move, try again.")
            continue
        board[move] = "X"
        print_board(board)

        if check_winner(board): break

        ai_move(board)
        print("Computer plays:")
        print_board(board)

        if check_winner(board): break

    result = check_winner(board)
    
    if result == "Draw":
        print("🤝 It's a Draw!")
    elif result == "O":
        print("🏆 AI wins!")
    elif result == "X":
        print("🏆 You win!")
play_game()
