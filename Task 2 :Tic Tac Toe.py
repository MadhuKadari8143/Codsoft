import math

# Initialize the board
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def make_move(position, player):
    board[position] = player

def winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def is_full():
    return " " not in board

def minimax(player):
    max_player = "O"  # AI
    other_player = "X" if player == "O" else "O"

    # Base cases
    if winner(other_player):
        return {"position": None, "score": 1 * (len(available_moves()) + 1) if other_player == max_player else -1 * (len(available_moves()) + 1)}
    elif is_full():
        return {"position": None, "score": 0}

    # Recursive case
    if player == max_player:
        best = {"position": None, "score": -math.inf}
    else:
        best = {"position": None, "score": math.inf}

    for move in available_moves():
        board[move] = player
        sim_score = minimax(other_player)
        board[move] = " "  # undo move
        sim_score["position"] = move

        if player == max_player:
            if sim_score["score"] > best["score"]:
                best = sim_score
        else:
            if sim_score["score"] < best["score"]:
                best = sim_score

    return best

def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Player move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        make_move(move, "X")
        print_board()

        if winner("X"):
            print("You win!")
            break
        if is_full():
            print("It's a tie!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = minimax("O")["position"]
        make_move(ai_move, "O")
        print_board()

        if winner("O"):
            print("AI wins!")
            break
        if is_full():
            print("It's a tie!")
            break

play_game()
