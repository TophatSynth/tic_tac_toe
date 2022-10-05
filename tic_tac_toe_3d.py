from random import choice

class TicTacToe():
    def __init__(self) -> None:
        self.board = []
        self.players = ["X", "O"]
        self.current_player = ""

    def print_intro(self) -> None:
        # Prints the intro/explanation everytime the game is restarted/reloaded

        print("""Welcome! ...""")

    def random_player_start(self) -> None:
        # Selects a random player to go first
        
        self.current_player = choice(self.players)

    def print_player_start(self) -> None:
        # Prints which player will be starting first

        print(f"{self.current_player} starts first! ")

    def create_board(self) -> None:
        # Creates the 3 x 3 x 3 board in columns, rows, and pancakes in that order
        
        for i in range(3):
            pancake = []
            for j in range(3):
                row = []
                for k in range(3):
                    row.append("-")
                pancake.append(row)
            self.board.append(pancake)

    def print_board(self) -> None:
        # Prints the board

        for beeg_row in self.board:
            row = 0 
            for pan in self.board:
                for col in pan[row]:
                    print(col, end=" ")
                print(" | ")
            row += 1

    def get_player_input(self) -> str:
        # Retrieves the player input and returns it as a string

        return list(map(int,input(f"Player {self.current_player}'s turn: ").split()))        

    def is_player_input_valid(self, player_input: list) -> bool:
        pass

    def save_player_input(self, player_input) -> None:
        # Saves the player choice on the board. Assumes that the choice is 100% valid (w/o non ints, is within range, has correct number of values, not placing over each other)

        pan, row, col = player_input
        self.board[pan][row][col] = self.current_player        

    def check_for_win(self) -> bool:
        # Checks the board for winning combinations (Horizontally, Vertically, Pancake-y, diagonally)

        for pan in self.board:
            # Horizontal flat
            for row in pan:
                if row[0] == row [1] == row[2]:
                    return True
            # Vertical flat
            for col in range(3):
                if pan[0][col] == pan[1][col] == pan[2][col]:
                    return True
            # Diagonal flat (top left to bottom right)
            if pan[0][0] == pan[1][1] == pan[2][2]:
                return True
            # Diagonal flat (top right bottom left)
            if pan[0][2] == pan[1][1] == pan[2][0]:
                return True
            
        for row in self.board[0]:
            for col in row:
                # Vertical vertical
                if self.board[0][row][col] == self.board[1][row][col] == self.board[2][row][col]:
                    return True
            # Diagonal vertical (bottom left to top right) 
            if self.board[0][row][0] == self.board[0][row][1] == self.board[0][row][2]:
                return True
            
            # Diagonal vertical (bottom right to top left)
            if self.board[0][row][2] == self.board[1][row][1] == self.board[2][row][0]:
                return True
            
        for col in self.board[0][0]:
            # Vertical vertical (bottom top to top bottom)
            if self.board[0][0][col] == self.board[1][1][col] == self.board[2][2][col]:
                return True
            # Vertical vertical (bottom bottom to top top)
            if self.board[0][2][col] == self.board[1][1][col] == self.board[2][0][col]:
                return True
        
        # Diagonal diagonal (bottom top left to top bottom right)
        if self.board[0][0][0] == self.board[1][1][1] == self.board[2][2][2]:
            return True
        # Diagonal diagonal (bottom top right to top bottom left)
        if self.board[0][0][2] == self.board[1][1][1] == self.board[2][2][0]:
            return True
        # Diagonal diagonal (bottom bottom left to top top right)
        if self.board[0][2][0] == self.board[1][1][1] == self.board[2][0][2]:
            return True
        # Diagonal diagonal (bottom bottom right to top top left)
        if self.board[0][0][2] == self.board[1][1][1] == self.board[2][0][0]:
            return True 
                            

    def print_player_win(self) -> None:
        print(f"Player {self.current_player} won !!!! ")

    def get_player_restart(self) -> str:
        pass

    def check_restart_valid(self, player_restart:str) -> bool:
        pass

    def check_for_draw(self) -> bool:
        # Checks for draws, outputs True if found
        pass

    def print_draw(self) -> None:
        # Prints the draw text

        print("It's a Draw! ")

    def swap_players(self) -> None:
        # Swaps the player from the current one

        self.current_player = "X" if self.current_player == "O" else "O"

    def start_game(self) -> None:
        # Runs and loops the game :D

        while True:
            self.print_intro()

            self.random_player_start()
            self.print_player_start

            self.create_board()

            while True:
                self.print_board()
                player_input = self.get_player_input()
                
                if self.is_player_input_valid(player_input=player_input):
                    self.save_player_input(player_input=player_input)
                
                if self.check_for_win():
                    self.print_player_win()
                    break

                if self.check_for_draw():
                    self.print_draw()
                    break

                self.swap_players()
            
            player_restart = self.get_player_restart()
            if self.check_restart_valid(player_restart=player_restart):
                if player_restart == "y":
                    pass
                else: 
                    break
            
tictactoe = TicTacToe()
tictactoe.start_game()