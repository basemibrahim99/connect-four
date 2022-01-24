import random


class ConnectFour:

    # Setting class constants which will be reused
    # throughout the code to eliminate magic numbers

    OPEN_SPACE = "⚪️"
    PLAYER_ONE_PIECE = "🔴"
    PLAYER_TWO_PIECE = "🟡"

    ROW_COUNT = 6
    COL_COUNT = 7
    TOP_ROW_INDEX = ROW_COUNT - 1
    LAST_COL_INDEX = COL_COUNT - 1
    MIDDLE_COL = 3

    # Init function to create the board and store the move count of the current game
    def __init__(self) -> None:

        self.board = self.create_board()
        self.move_count = 0

    # Creating the game board using a 2D array
    # Returns the board.
    def create_board(self):

        return [
            [self.OPEN_SPACE for i in range(self.COL_COUNT)]
            for i in range(self.ROW_COUNT)
        ]

    # Printing the board in an aesthetic fashion with numbered columns
    def print_board(self):

        print("")
        for row in range(self.ROW_COUNT - 1, -1, -1):
            print(*self.board[row], sep="|")
        print("0️⃣ |1️⃣ |2️⃣ |3️⃣ |4️⃣ |5️⃣ |6️⃣ \n")

    # Validating the user input to confirm that it is a valid
    # column number and that the column itself is not full.
    # Returns a boolean.
    def valid_user_input(self, col):

        if not col.isdigit():
            return False
        col = int(col)
        if (0 <= col <= 6) and self.board[self.TOP_ROW_INDEX][col] == self.OPEN_SPACE:
            return True
        else:
            return False

    # Validating the input of the selected type of game
    # Two selections are valid, 'R' for random input  and 'U' for user input.
    # Returns a boolean.
    def validate_type_of_game(self, type_of_game):

        if type_of_game.upper() in ["R", "U"]:
            return True
        else:
            return False

    # Validating the randomly generated column number
    # to confirm that the column itself is not full.
    # Returns a boolean.
    def valid_random_input(self, col):

        return self.board[self.TOP_ROW_INDEX][col] == self.OPEN_SPACE

    # Finding the next open row in a validated given column.
    # Returns the row index.
    def get_next_open_row(self, col):

        for row in range(self.ROW_COUNT):
            if self.board[row][col] == self.OPEN_SPACE:
                return row

    # Inserts the piece of a player into the next open row
    # in a validated column and increments the move count.
    def drop_piece(self, row, col, piece):

        self.board[row][col] = piece
        self.move_count += 1

    # Given a player number, sets the piece variable and prompts the user for their column choice
    # Keeps prompting the user for a valid input until one is given
    # Finds the next open row in the valid column and drops the piece into that position
    # Returns a boolean of whether that given move was a game winning move
    def play_turn(self, player_number):

        piece = self.PLAYER_ONE_PIECE if player_number == 1 else self.PLAYER_TWO_PIECE
        col = input(f"Player {player_number}, make your move (0-6): ")
        while not self.valid_user_input(col):
            col = input(f"Player {player_number}, make a VALID move (0-6): ")
        col = int(col)
        row = self.get_next_open_row(col)
        self.drop_piece(row, col, piece)
        return self.winning_move(row, col, piece)

    # Similar to the play_turn() function above but instead of a manual input
    # The column of choice is randomly generated using the randint() method of random
    def play_turn_random(self, player_number):

        piece = self.PLAYER_ONE_PIECE if player_number == 1 else self.PLAYER_TWO_PIECE
        input(f"Player {player_number}, make your move (0-6): ")
        col = random.randint(0, 6)
        while not self.valid_random_input(col):
            input(f"Player {player_number}, make a VALID move (0-6): ")
            col = random.randint(0, 6)
        row = self.get_next_open_row(col)
        self.drop_piece(row, col, piece)
        return self.winning_move(row, col, piece)

    # Checks if the last move caused a vertical connect-four win
    # Returns a boolean
    def vertical_win(self, row, col, piece):
        if row < 3:
            return False
        for i in range(4):
            if self.board[row - i][col] != piece:
                return False
        return True

    # Checks if the last move caused a horizontal connect-four win
    # Returns a boolean
    def horiztonal_win(self, row, col, piece):

        start = col
        curr_col = col - 1

        while curr_col >= 0 and self.board[row][curr_col] == piece:
            start = curr_col
            curr_col -= 1

        end = col
        curr_col = col + 1
        while (
            curr_col <= self.LAST_COL_INDEX
            and self.board[row][curr_col] == piece
            and (end - start < 3)
        ):
            end = curr_col
            curr_col += 1

        return end - start >= 3

    # Checks if the last move caused a positively sloped connect-four win
    # Returns a boolean
    def positive_diagonal_win(self, row, col, piece):

        start = col
        curr_col = col - 1
        curr_row = row - 1

        while (
            curr_col >= 0 and curr_row >= 0 and self.board[curr_row][curr_col] == piece
        ):
            start = curr_col
            curr_col -= 1
            curr_row -= 1

        end = col
        curr_col = col + 1
        curr_row = row + 1

        while (
            curr_col <= self.LAST_COL_INDEX
            and curr_row <= self.TOP_ROW_INDEX
            and self.board[curr_row][curr_col] == piece
            and (end - start < 3)
        ):
            end = curr_col
            curr_col += 1
            curr_row += 1

        return end - start >= 3

    # Checks if the last move caused a negatively sloped connect-four win
    def negative_diagonal_win(self, row, col, piece):

        start = col
        curr_col = col - 1
        curr_row = row + 1

        while (
            curr_col >= 0
            and curr_row <= self.TOP_ROW_INDEX
            and self.board[curr_row][curr_col] == piece
        ):
            start = curr_col
            curr_col -= 1
            curr_row += 1

        end = col
        curr_col = col + 1
        curr_row = row - 1

        while (
            curr_col <= self.LAST_COL_INDEX
            and curr_row >= 0
            and self.board[curr_row][curr_col] == piece
            and (end - start < 3)
        ):
            end = curr_col
            curr_col += 1
            curr_row -= 1

        return end - start >= 3

    # Checks if the last move caused any of the four possible win scenarios
    # Returns a boolean
    def winning_move(self, row, col, piece):

        return (
            self.vertical_win(row, col, piece)
            or self.horiztonal_win(row, col, piece)
            or self.positive_diagonal_win(row, col, piece)
            or self.negative_diagonal_win(row, col, piece)
        )

    # This is the main method which starts the game up.
    # First by prompting the user to select which type of game they would like to play (Random or User Inputted).
    # Next the game_over variable is set to False, turn is set to 1 and the game board is printed to the console.
    # The turn variable flips between -1 and 1 to determine which player's turn it is to go.
    # The main game loop then begins, calling the functions above in a logical order for smooth game play.
    # The loop exits when either a win is found or the board completly fills up (which sets game_over to True).
    def play(self):

        type_of_game = input(
            'Press "R" for a randomally inputted game or "U" for a user inputted game: '
        )
        while not self.validate_type_of_game(type_of_game):
            type_of_game = input(
                'Invalid input!\nPress "R" for a randomally inputted game or "U" for a user inputted game: '
            )

        game_over = False
        turn = 1
        self.print_board()

        while not game_over:

            player_number = 1 if turn > 0 else 2
            winning_move = (
                self.play_turn(player_number)
                if type_of_game.upper() == "U"
                else self.play_turn_random(player_number)
            )

            if winning_move:
                game_over = True
                print(f"Game Over!\nPlayer {player_number} wins!")

            if self.move_count == self.ROW_COUNT * self.COL_COUNT:
                game_over = True
                print("Game Over! The board is full!")

            self.print_board()
            turn = turn * -1


game = ConnectFour()
game.play()
