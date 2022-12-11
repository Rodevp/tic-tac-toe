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

    position = input("Enter position 1 - 9: ")

    if position >= 1 and position <= 9 and board[position - 1] == "-" :
        board[position - 1] = current_player
    else :
        print("Oops!, position is ocuped")


def check_matchs_rows(board) :

    if board[0] == board[1] == board[2] and board[0] != "-" :
        change_winner(True)
        return True

    if board[3] == board[4] == board[5] and board[3] != "-" :
        change_winner(True)
        return True

    if board[2] == board[5] == board[8] and board[2] != "-" :
        change_winner(True)
        return True


def main() :
    pass



if __name__ == "__main__" :
    main()

