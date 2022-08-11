import random
from time import sleep

class TicTacToe():

    def __init__(self) -> None:
        self.board = []

    def create_board(self) -> None:
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
    
    def display_board(self) -> None:
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def grab_player_choice(self) -> list:
        return list(map(int, input(f"Player {self.player}'s turn: ").split()))
        
        
    def save_player_choice(self, choices:list) -> None:
        row, col = choices
        self.board[row-1][col-1] = self.player
            

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
        
    def choose_random_player(self) -> None:
        self.player = random.choice(["X", "O"])
        print(f"Player {self.player} goes first! \n")
    
    def swap_turns(self):
        self.player = "X" if self.player == "O" else "O"
    
    def display_intro(self) -> None:
        print("""Tic Tac Toe Game
        
Each player chooses X or O
        
For each turn, type the row then column of your choice like this: row column

eg: 1 3 

This will display:

- - X
- - -
- - -
(row 1, column 3)
        
We will start the game now. 
""")
    
    def display_win(self) -> None:
        print(f"{self.player} won!! Congratulations! \n")

    def display_draw(self) -> None:
        print("It's a draw! \n")

    def restart_confirmation(self) -> bool:
        return True if input("Would you like to restart? (y/n)") == "y" else False
    
    def display_end(self) -> None:
        print("Thank you for playing! :D")

    def start_game(self) -> None:
        while True:
            self.display_intro()

            sleep(1)

            self.create_board()
            self.choose_random_player()

            while True:
                self.display_board()
                choices = self.grab_player_choice()
                print()
                self.save_player_choice(choices)

                if self.check_for_win():
                    self.display_win()
                    break
                elif self.check_filled():
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