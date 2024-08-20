class Tictactoe:

    def __init__(self,playerone,playertwo):
        self.playerone = playerone
        self.playertwo = playertwo
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
        print("Coordinates must range from 0 to 2, 0 corresponding to the first row/column, onwards")
        xcoor = int(input("What is your x coordinate?:"))
        ycoor = int(input("What is your y coordinate?:"))
        
        if xcoor not in {0,1,2} or ycoor not in {0,1,2}:
            print("Coordinates must be between 0 and 2")
            
        
        return xcoor,ycoor


    def makeMove(self):

        marker = "O"
        
        xcoor,ycoor = self.getMove()

        
        

        #if first move, make the move
        if len(self.made_moves)== 0:
            self.board[xcoor][ycoor] = marker
            self.made_moves.append((xcoor,ycoor))
        
        
        #for all other moves, check to see if the position is filled
        else:
            if (xcoor,ycoor) in self.made_moves:
                print(f"The position at {xcoor,ycoor} is already full, please try again.")
            else:
                self.board[xcoor][ycoor] = marker
                self.made_moves.append((xcoor,ycoor))

        return
            




    def getWinner(self):
        #todo write win conditions
        '''if player one marks 3 in a row, player one wins, end game
        if player two marks 3 in a row, player 2 wins, end game
        '''
        pass

    def resetButton(self):
        #todo: create a reset button that clears the board.
        pass

    def runGame(self):
        test = Tictactoe("playerone", "playertwo")
        print(test.newBoard())
        for i in range(9):
            print(test.makeMove())
            print(test.renderBoard())
        return (f"Game Over, it is a draw")
        
    

    def isBoardFull(self):
        #todo: write code that checks if board is full
        pass


def main():
    test = Tictactoe("playerone", "playertwo",)
    print(test.runGame())

if __name__ == '__main__':
    main()