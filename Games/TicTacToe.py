import random

class TicTacToe():

    def __init__(self, aiUse = False):
        """
        Initialize a new board. Default mode is two-player, enter parameter
        'True' for board use with AI.
        """
        # Create board
        self.board = []
        for row in range(3): # 3 Rows
            aRow = []
            for col in range(3): # 3 Columns
                aCol = " "
                aRow.append(aCol)
            self.board.append(aRow)
        self.isComplete = False

        # Create players
        self.player1 = "X"
        self.player2 = "O"
        self.playerTurn = self.player1
        self.aiUse = aiUse

    def switchPlayer(self):
        """
        Changes the current player status. This will allow for
        placement of both player pieces.
        :return: none
        """
        # Switch player turn
        if(self.playerTurn == self.player1 ):
            self.playerTurn = self.player2
        else:
            self.playerTurn = self.player1

    def commandListener(self):
        """
        Allows the user to enter a command and will call an appropriate
        function corresponding to the command, otherwise the function
        will recall itself until a valid command is given
        :return: None
        """
        # List Valid Inputs
        generalCommands = ["q"]

        # Get User Input
        print("Player {}'s turn: ".format(self.playerTurn))
        userInput = input()

        # Test User Input
        try:
            userInput = int(userInput)
            self.placePiece(userInput)
        except:
            if(userInput in generalCommands ):
                if(userInput == "q"):
                    self.quitGame()
            else:
                print("Sorry, invalid command!\n")
                self.commandListener()



    def quitGame(self):
        self.isComplete = True



    def __str__(self):
        """
        Creates a string representation of the tic tac toe board.
        This means a grid and player pieces will be displayed.
        :return: String representation of the game board
        """
        rtrnStr = ""
        colCount = 0
        for row in self.board:
            rowCount = 0
            for spot in row:
                rtrnStr += str(spot)
                if(rowCount < 2 ):
                    rtrnStr += " | "
                rowCount += 1
            if(colCount < 2):
                rtrnStr += "\n---------\n"
            colCount += 1
        rtrnStr += "\n\n"
        return rtrnStr


    def placePiece(self, spot):
        if( 0 > spot or spot > 9 ):
            print("Invalid Placement")
            print("Hint: Try values 1 - 9")
            self.commandListener()

        else:
            spot -= 1
            row = spot // 3
            col = spot % 3
            if(self.board[row][col] == " "):
                self.board[row][col] = self.playerTurn
                self.switchPlayer()
            else:
                print("Not empty, try again")
                self.commandListener()




def main():

    aGame = TicTacToe(False)
    print(aGame)
    aGame.commandListener()
    print(aGame)
    aGame.commandListener()
    print(aGame)

if __name__ == '__main__':
    main()
