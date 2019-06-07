import random

class gameBoard():

    def __init__(self, aiUse = False):
        """
        Initialize a new board. Default mode is two-player, enter parameter
        'True' for board use with AI.
        """
        self.board = {1:" ", 2:" ", 3:" ",
                      4:" ", 5:" ", 6:" ",
                      7:" ", 8:" ", 9:" "}
        self.pieces = ["X", "O"]
        self.gameOver = False
        self.isPlayerOne = True
        self.aiUse = aiUse
        self.spotList = []
        iter = 0
        for iter in range(9):
            self.spotList.append(iter + 1)

    def placePiece(self, spot):
        """
        Places game piece in designated spot.
        Returns True if placement was successful.
        """
        player = 1
        if(self.isPlayerOne):
            player = 0
        piece = self.pieces[player]
        # Play pieces only in empty spots
        if spot in self.spotList:
            self.board[spot] = piece
            self.spotList.remove(spot)
            self.isPlayerOne = not self.isPlayerOne
            return True
        return False

    def checkRow(self):
        """
        Checks rows of the game board
        """
        check = False
        bd = self.board
        rows = [ [ bd[1], bd[2], bd[3] ],
                 [ bd[4], bd[5], bd[6] ],
                 [ bd[7], bd[8], bd[9] ] ]
        for row in rows:
            if(row[0] == row[1] == row[2] != " "):
                check = True
        return check

    def checkCol(self):
        """
        Checks columns of the game board
        """
        check = False
        bd = self.board
        cols = [ [ bd[1], bd[4], bd[7] ],
                 [ bd[2], bd[5], bd[8] ],
                 [ bd[3], bd[6], bd[9] ] ]
        for col in cols:
            if(col[0] == col[1] == col[2] != " "):
                check = True
        return check

    def checkDiag(self):
        """
        Checks both diagonals of the game board
        """
        check = False
        bd = self.board
        diagonals = [ [bd[1], bd[5], bd[9]],
                      [bd[3], bd[5], bd[7]] ]
        for diags in diagonals:
            if(diags[0] == diags[1] == diags[2] != " "):
                check = True
        return check

    def checkAll(self):
        """
        Calls all check methods and returns True if
        at least one method returns True.
        """
        if(self.checkRow() or self.checkCol() or self.checkDiag()):
            return True
        return False

    def aiPlay(self):
        pass

    def testItem(self, userInput):
        """
        Tests input for valid placement or command
        """
        try:
            userInput = int(userInput)
        except:
            if userInput.lower() != 'q':
                print("Invalid Command")
        return userInput

    def getInput(self):
        """

        """
        playerStr = "1: "
        if(not self.isPlayerOne):
            playerStr = "2: "
        print("Player {} ".format(playerStr))
        newCommand = input("--> ")
        newCommand = self.testItem(newCommand)
        return newCommand

    def __str__(self):
        board = self.board
        strDef = " {} | {} | {}\n".format(board[1], board[2], board[3]) +\
                 "-----------\n" +\
                 " {} | {} | {}\n".format(board[4], board[5], board[6]) +\
                 "-----------\n" +\
                 " {} | {} | {}\n".format(board[7], board[8], board[9])
        return strDef

# Initialize Game
aGame = gameBoard()
gameQuit = ""
gameFin = False
print(aGame)
while(gameQuit != "q" and gameQuit != "n"):
    gameQuit = aGame.getInput()
    if(isinstance(gameQuit, int)):
        placeSuccess = aGame.placePiece(gameQuit)
        if (placeSuccess):
            print(aGame)
            gameFin = aGame.checkAll()
            print(gameFin)
