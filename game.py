board_initial = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

current_player = "X"
winner = None
game_running = True

def change_winner(is_winner) :
    global winner
    winner = is_winner
    return winner


def print_board(board) :
    
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_into_X_or_O(board) :

    position = int( input("Enter position 1 - 9: ") )

    if position >= 1 and position <= 9 and board[position - 1] == "-" :
        board[position - 1] = current_player
    else :
        print("Oops!, position is ocuped")


def check_matchs_rows(board) :

    if board[0] == board[1] == board[2] and board[0] != "-" :
        change_winner(board[0])
        return True

    if board[3] == board[4] == board[5] and board[3] != "-" :
        change_winner(board[3])
        return True

    if board[2] == board[5] == board[8] and board[2] != "-" :
        change_winner(board[2])
        return True


def check_diagonals(board) :

    if board[0] == board[4] == board[5] and board[0] != "-":
        change_winner(board[0])
        return True

    if board[2] == board[4] == board[6] and board[2] != "-" :
        change_winner(board[2])
        return True


def check_columns(board):

    if board[0] == board[3] == board[6] and board[0] != "-":
        change_winner(current_player)
        return True

    if board[1] == board[4] == board[7] and board[1] != "-" :
        change_winner(current_player)
        return True

    if board[2] == board[5] == board[8] and board[2] != "-" :
        change_winner(current_player)
        return True


def check_tie(board) :

    global game_running
    if  not "-" in board :
        print_board(board)
        print("---results---")
        game_running = False


def valid_player() :

    global current_player
    if current_player == "X" :
        current_player = "O"
    else :
        current_player = "X"


def check_win():
    if check_matchs_rows(board_initial) or check_diagonals(board_initial) or check_columns(board_initial):
        print(f"The winner is {winner}")


def main() :
    while game_running :
        print_board(board_initial)
        player_into_X_or_O(board_initial)
        check_win()
        check_tie(board_initial)
        valid_player()



if __name__ == "__main__" :
    main()

