class Tictactoe:

    def __init__(self):
        self.current_player = "X"
        self.players = ["X", "O"]
        self.made_moves = []
        
        
        
        

    def newBoard(self):
        # creates new board
        self.board = [[None, None, None],
                 [None, None, None],
                 [None, None, None]
                 ]
        
        

    def renderBoard(self):
        # Prints current state of the board
        for row in self.board:
            print("|", end="")
            for cell in row:
                if cell is None:
                    print("   |", end="")
                else:
                    print(f" {cell} |", end="")
            print("\n" + "-" * 13)

    


    def getMove(self):
        while True:
            try:
                print("Coordinates must range from 0 to 2, 0 corresponding to the first row/column, onwards")
                xcoor = int(input("What is your x coordinate?:"))
                ycoor = int(input("What is your y coordinate?:"))
        
                if xcoor in {0,1,2} or ycoor in {0,1,2}:
                    if (xcoor,ycoor) in self.made_moves:
                        print(f"The position at {xcoor,ycoor} is already full, please try again")
                    else:
                        return xcoor, ycoor
                    
                else:
                    print("Coordinates must be between 0 and 2.")
            except ValueError:
                print("Invalid input, please only enter integers.")
                    


    def makeMove(self):
        xcoor, ycoor = self.getMove()
        self.board[xcoor][ycoor] = self.current_player
        self.made_moves.append((xcoor, ycoor))
        if self.getWinner():  # Check for a winner after every move
            self.renderBoard()
            print(f"Game Over! Player {self.current_player} wins!")
            return True
        self.switchPlayer()
        return False

    #ternary operator that alternates between players
    def switchPlayer(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def getWinner(self):
        # Define winning combinations
        winning_combinations = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        # Check each winning combination
        for combination in winning_combinations:
            if all(self.board[x][y] == self.current_player for x, y in combination):
                return True
        
        return False

    def resetButton(self):
        #todo: create a reset button that clears the board.
        pass
    
    def isBoardFull(self):
        return len(self.made_moves) == 9


    def runGame(self):
        self.newBoard()  # Initialize the board
        for i in range(9):
            if self.makeMove():  # Check if the game was won
                return  # Stop running if there's a winner
            self.renderBoard()
            if self.isBoardFull():
                print("Game Over, it is a draw!")
                return
        

def main():
    test = Tictactoe()
    print(test.runGame())

if __name__ == '__main__':
    main()