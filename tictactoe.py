import random
from time import sleep

class TicTacToe():

    def __init__(self) -> None:
        self.board = []

    # Creating the board

    def create_board(self) -> None:
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    # Player turns

    def choose_random_player(self) -> None:
        self.player = random.choice(["X", "O"])
        print(f"Player {self.player} goes first! \n")
    
    def swap_turns(self):
        self.player = "X" if self.player == "O" else "O"

    # Display functions 
    
    def display_board(self) -> None:
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def display_intro(self) -> None:
        print("""- - - - - - -

Tic Tac Toe Game
        
Each player chooses X or O
        
For each turn, type the row then column of your choice like this: row column

eg: 1 3 

This will display:

- - X
- - -
- - -
(row 1, column 3)
        
We will start the game now. 

- - - - - - -
""")
    
    def display_win(self) -> None:
        print(f"{self.player} won!! Congratulations! \n")

    def display_draw(self) -> None:
        print("It's a draw! \n")
    
    def display_end(self) -> None:
        print("\nThank you for playing! :D \n")

    # Player choice inputs

    def grab_player_choice(self) -> list:
        try: 
            return list(map(int, input(f"Player {self.player}'s turn: ").split()))
        except ValueError:
            return False
        
    def save_player_choice(self, choices:list) -> None:
        row, col = choices
        self.board[row-1][col-1] = self.player

    def is_player_choice_valid(self, choices:list) -> list:
        try:
            row, col = choices
            return [True] if self.board[row-1][col-1] == "-" else [False, "That space is already filled! Try again \n"]
        except ValueError:
            return [False, "Missing row or column! Try again \n"] if len(choices) < 2 else [False, "Too many values! Try again \n"]
        except TypeError:
            return [False, "That's not a number! Try again \n"]            
        except IndexError:
            return [False, "That's not within the board! Try again \n"]
    
    def player_choice_not_valid(self, error_msg:list) -> None:
        print(error_msg[1])
            
    # Checking the board

    def check_for_win(self) -> bool:
        win = True

        for i in range(3):
            win = True
            for j in range(3):
                if self.board[i][j] != self.player:
                    win = False
                    break
            if win: 
                return win
        win = True
        
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != self.player:
                    win = False
                    break
            if win:
                return win
        win = True

        for i in range(3):
            if self.board[i][i] != self.player:
                win = False
        if win:
            return win
        win = True

        for i in range(3):
            if self.board[i][3 - 1 - i] != self.player:
                win = False
                break
        if win:
            return win
        return False

    def check_filled(self) -> bool:
        for row in self.board:
            for item in row:
                if item == "-":
                    return False
        return True

    # Check to restart the game    

    def restart_confirmation(self) -> bool:
        return True if input("Would you like to restart? (y/n): ") == "y" else False
    
    # Main function

    def start_game(self) -> None:
        while True:
            self.display_intro()

            self.create_board()
            self.choose_random_player()

            while True:
                self.display_board()
                choices = self.grab_player_choice()
                print()
                error = self.is_player_choice_valid(choices)
                if error[0]:
                    self.save_player_choice(choices)
                else:
                    self.player_choice_not_valid(error)
                    continue

                if self.check_for_win():
                    self.display_board()
                    self.display_win()
                    break
                elif self.check_filled():
                    self.display_board()
                    self.display_draw()
                    break
                
                self.swap_turns()
            
            if self.restart_confirmation():
                print()
                pass
            else:
                self.display_end()
                break
        

tictactoe = TicTacToe()
tictactoe.start_game()