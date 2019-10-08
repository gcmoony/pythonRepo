import random

class TicTacToe():
    """
    This is a simple user input style Tic-Tac-Toe game. This can be played
    with one or two players.

    Attributes:
            aiUse (Boolean): Single player mode has been chosen, and an
                             AI will be enabled to play against the player
    """

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
        print() # New Line

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

    def isRunning(self):
        """
        Checks to see if the game is still currently running
        :return: A boolean representation of the running game
        """
        return not self.isComplete

    def quitGame(self):
        """
        Ends the current game
        :return: none
        """
        self.isComplete = True

    def checkRows(self):
        """
        Checks all the rows of the game board
        to see if all spaces in a single row contain
        the same game piece.
        If a winner is found, method will quit the game
        :return: None
        """
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                self.quitGame()
                print("\n\n{} won!".format(row[0]))
                print("Game Over\n")

    def checkCols(self):
        """
        Checks all the rows of the game board
        to see if all spaces in a single column contain
        the same game piece.
        If a winner is found, method will quit the game
        :return: None
        """
        for col in range(3):
            if self.board[0][col] == self.board[1][col]\
                == self.board[2][col] != " ":
                self.quitGame()
                print("\n\n{} won!".format(self.board[0][col]))
                print("Game Over\n")

    def checkDiag(self):
        """
        Checks both diagonals of the board to see if the pieces placed within
        are matching game pieces.
        If a winner is found, method will quit the game
        :return: None
        """
        bd = self.board
        if(bd[0][0] == bd[1][1] == bd[2][2] != " " or\
                bd[0][2] == bd[1][1] == bd[2][0] != " "):
            self.quitGame()
            print("\n\n{} won!".format(bd[1][1]))
            print("Game Over\n")

    def checkBoard(self):
        bd = self.board
        emptySpotExists = False
        for row in bd:
            if " " in row:
                emptySpotExists = True
        if(emptySpotExists == False):
            self.quitGame()
            print("\n\nGame Over!")
            print("No winner here today...")

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
        """
        Tests a given spot for correct board piece placement. If a spot is vacant,
        the designated player piece will be placed on the board. If the spot is full,
        the method will display an error message
        :param spot: An integer representation of a valid spot on the game board
        :return: None
        """
        if( 0 >= spot or spot > 9 ):
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
    while(aGame.isRunning()):
        print(aGame)
        aGame.commandListener()
        aGame.checkRows()
        aGame.checkCols()
        aGame.checkDiag()
        aGame.checkBoard()
    print(aGame)

if __name__ == '__main__':
    main()
