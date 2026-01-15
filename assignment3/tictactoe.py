# Task 6: More on Classes

# custom exception
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
     valid_moves=["upper left", "upper center", "upper right", 
                  "middle left", "center", "middle right", 
                  "lower left", "lower center", "lower right"]
     
     def __init__(self):
         self.board_array = [[" " for _ in range (3)] for _ in range(3)]
         self.turn = "X"
         self.last_move = None

     def __str__(self):
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    
     def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        
        # switch turn
        self.turn = "O" if self.turn == "X" else "X"
     
     def whats_next(self):
        win = False
        # A. check for a win
        # rows
        for i in range(3): # check rows
            if self.board_array[i][0] != " " and self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break 
            
        # check columns
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " " and self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:   
                        win = True
                        break
                
        # check diagonals
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] == self.board_array[2][2]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] == self.board_array[2][0]:
                    win = True
        
        # if someone won the game, check who won the game
        if win:
            Winner = "O" if self.turn == "X" else "X"
            return (True, f"{Winner} wins!")

        # check for Cat's game (board full)
        if all(self.board_array[i][j] != " " for i in range(3) for j in range (3)):
            return (True, "Cat's game.")
        
        # otherwise, game continues
        return (False, f"{self.turn}'s turn.")

# Main game loop            
if __name__ == "__main__":
    board = Board()
    print("Welcome to Tictactoe \n")
    print(board)

    while True:
        # ask for a move:
        print(board.whats_next()[1])
        move = input("Please enter your move: ").strip() # strip remove any extra spaces
        
        print(f"{board.turn}'s move. Valid moves: {Board.valid_moves} ")
        
        try:
            board.move(move)
            print(board) # I want to see the board after each move
        except TictactoeException as e:
            print(f"Error: {e.message}")

        # check game status:
        over, status = board.whats_next()
        if (over):
            print(status)
            break

          
