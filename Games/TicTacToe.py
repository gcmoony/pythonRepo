import random

class gameBoard():

    def __init__(self):
        self.board = {1:" ", 2:" ", 3:" ",
                      4:" ", 5:" ", 6:" ",
                      7:" ", 8:" ", 9:" "}
        self.pieces = ["X", "O"]
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
newGame = gameBoard()
print(newGame)
print(newGame.spotList)
newGame.placePiece(0, 3)
print(newGame)
print(newGame.spotList)
newGame.placePiece(1, 5)
print(newGame)
print(newGame.spotList)
