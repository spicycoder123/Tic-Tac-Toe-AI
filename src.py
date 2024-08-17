
class Tictactoe:

    def __init__(self, playerone, playertwo,):
        self.playerone = playerone
        self.playertwo = playertwo
        
        

    def newBoard(self):
        # creates new board
        return [[None, None, None],
                 [None, None, None],
                 [None, None, None]
                 ]
        
        
        
        


    def renderBoard(self):
        board = self.newBoard()
        
        # Prints current state of the board
        for row in board:
            print("|", end="")
            for cell in row:
                if cell is None:
                    print("   |", end="")
                else:
                    print(f" {cell} |", end="")
            print("\n" + "-" * 13)



    def getMove(self):
        #todo: get inputfor current player's move
        pass

    def makeMove(self):
        #todo: code the current player's move
        pass

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
        #todo: write code that starts the game.
        pass

    def isBoardFull(self):
        #todo: write code that checks if board is full
        pass


def main():
    test = Tictactoe("playerone", "playertwo")
    test.renderBoard()

if __name__ == '__main__':
    main()