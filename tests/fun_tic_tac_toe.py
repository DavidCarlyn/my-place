from enum import Enum
from dataclasses import dataclass
import random

class Mark(Enum):
    X = "X"
    O = "O"
    BLANK = " "

@dataclass
class Position:
    row: int = 0
    col: int = 0

class Board:
    def __init__(self):
        self.state = [
            [Mark.BLANK, Mark.BLANK, Mark.BLANK],
            [Mark.BLANK, Mark.BLANK, Mark.BLANK],
            [Mark.BLANK, Mark.BLANK, Mark.BLANK]
        ]
        
        self.end_game_state = None
            
    def play(self):
        print("Welcome to the game")
        
        self.print_board()
        while not self.is_end_game():
            print("please mark a position")
            input_str = input()
            row = int(input_str[0])
            col = int(input_str[1])
            
            current_position_state = self.state[row][col]
            if  current_position_state != Mark.BLANK:
                print("Invalid position")
                continue
            
            self.state[row][col] = Mark.X
            
            self.update_end_game()
            if self.is_end_game():
                break
            
            positions = self.get_unmarked_positions()
            
            pos = random.choice(positions)
            
            self.state[pos.row][pos.col] = Mark.O
            
            self.update_end_game()
            
            self.print_board()
            
        print(f"Game over! {self.end_game_state} won the game!")
    
    def print_board(self):
        for row in range(3):
            row_str = "|"
            for col in range(3):
                row_str += str(self.state[row][col]) + "|"
            print(row_str)
            
    def get_unmarked_positions(self):
        unmarked = []
        for row in range(3):
            for col in range(3):
                if self.state[row][col] == Mark.BLANK:
                    unmarked.append(Position(row=row, col=col))
        return unmarked
    
    def update_end_game(self):
        if len(self.get_unmarked_positions()) == 0:
            self.end_game_state = "Cat"
            
        # Check rows
        for row in range(3):
            check = None
            for col in range(3):
                pos_state = self.state[row][col]
                if pos_state == Mark.BLANK: 
                    check = None
                    break
                if check is None:
                    check = pos_state
                elif check != pos_state: 
                    check = None
                    break
            if check is not None:
                self.end_game_state = check
                return
        
        # Check cols
        for col in range(3):
            check = None
            for row in range(3):
                pos_state = self.state[row][col]
                if pos_state == Mark.BLANK: 
                    check = None
                    break
                if check is None:
                    check = pos_state
                elif check != pos_state: 
                    check = None
                    break
            if check is not None:
                self.end_game_state = check
                return
                
        # check diag 1
        check = None
        for i in range(3):
            pos_state = self.state[i][i]
            if pos_state == Mark.BLANK: 
                check = None
                break
            if check is None:
                check = pos_state
            elif check != pos_state: 
                check = None
                break
        if check is not None:
            self.end_game_state = check
            return
        
        # check diag 2
        check = None
        for i in range(3):
            pos_state = self.state[2-i][2-i]
            if pos_state == Mark.BLANK: 
                check = None
                break
            if check is None:
                check = pos_state
            elif check != pos_state: 
                check = None
                break
        if check is not None:
            self.end_game_state = check
            return
    
    def is_end_game(self):
        if self.end_game_state is None:
            return False
        
        return True
        
    def add_mark(self, position: Position, mark: Mark):
        self.state[position.row, position.col] = mark

def main():
    board = Board()
    board.play()

if __name__ == "__main__":
    main()