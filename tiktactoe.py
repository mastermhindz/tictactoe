if __name__ == '__main__':
    board = [[' ' for x in range(3)] for y in range(3)]
    player = 'X'

    def print_board():
        for row in board:
            print(row)

    def check_win():
        # check rows
        for row in board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        # check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return True

        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True

        return False

    def check_tie():
        for row in board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def switch_player():
        global player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    def play():
        while True:
            print_board()

            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if board[row][col] != ' ':
                print("Position occupied, try again!")
                continue

            board[row][col] = player

            if check_win():
                print_board()
                print(player, "wins!")
                break

            if check_tie():
                print_board()
                print("It's a tie!")
                break

            switch_player()

    play()