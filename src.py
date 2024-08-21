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
        xcoor,ycoor = self.getMove()
        self.board[xcoor][ycoor] = self.current_player
        self.made_moves.append((xcoor,ycoor))
        self.switchPlayer()

    #ternary operator that alternates between players
    def switchPlayer(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def getWinner(self):
        #todo write win conditions
        '''if player one marks 3 in a row, player one wins, end game
        if player two marks 3 in a row, player 2 wins, end game
        '''
        pass

    def resetButton(self):
        #todo: create a reset button that clears the board.
        pass
    
    def isBoardFull(self):
        #todo: write code that checks if board is full
        pass

    def runGame(self):
        test = Tictactoe()
        test.newBoard()
        for i in range(9):
            test.makeMove()
            test.renderBoard()
        return (f"Game Over, it is a draw")
        

def main():
    test = Tictactoe()
    print(test.runGame())

if __name__ == '__main__':
    main()