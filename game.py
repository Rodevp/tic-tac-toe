def print_board() :
    board_initial = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

    print(board_initial[0] + " | " + board_initial[1] + " | " + board_initial[2])
    print("-" * 9)
    print(board_initial[3] + " | " + board_initial[4] + " | " + board_initial[5])
    print("-" * 9)
    print(board_initial[6] + " | " + board_initial[7] + " | " + board_initial[8])






def main() :
    print_board()



if __name__ == "__main__" :
    main()

