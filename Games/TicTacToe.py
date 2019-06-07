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

    def placePiece(self, player, spot):
        piece = self.pieces[player]
        # Play pieces only in empty spots
        if spot in self.spotList:
            self.board[spot] = piece
            self.spotList.remove(spot)

    def aiPlay(self):
        choice = 0
        while(choice not in self.spotList):
            random.randint(1, 9)

    def testItem(self, userInput):
        try:
            userInput = int(userInput)
            return userInput
        except:
            if userInput.lower() != 'q':
                print("Invalid Command")

    def getInput(self):
        playerStr = "1: "
        if(self.isPlayerOne):
            playerStr = "2: "
        newCommand = input("Player ", playerStr)
        self.isPlayerOne = not self.isPlayerOne

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
print(aGame)
