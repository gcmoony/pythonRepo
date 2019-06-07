import random

class gameBoard():

    def __init__(self, aiUse = False):
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

    def __str__(self):
        strDef = ""
        counter = 0
        sep = 0
        for spot in self.board:
            strDef += str(self.board[spot])
            counter += 1
            if counter == 3:
                counter = 0
                strDef += "\n"
                if sep < 2:
                    strDef += "----------\n"
                    sep += 1
            else:
                strDef += " | "
        strDef += "\n==============\n"
        return strDef

# Initialize Game
aGame = gameBoard()
gameQuit = ""
player = 0
print(aGame)
while(gameQuit != "q" and aGame.spotList != []):
    aGame.getInput()
