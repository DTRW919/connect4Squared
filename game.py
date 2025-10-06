from connectFour import ConnectFour
from player import Player


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.moves = 2  # Number of moves each player gets

        self.winner = 0

        self.connectFour = ConnectFour(self.player1, self.player2)

    def validateResponse(self, ansList, msg="", caseSensitive=False):
        userInput = ""  # Field to check what the user says
        count = -1  # Count number of tries; First one doesnt count

        # Lowercase list of answers if caseSensitive is true
        ansListLC = list(ans.lower() for ans in ansList if type(ans) is str)

        # If the response is not valid or for extra function
        while userInput not in (ansList if caseSensitive else ansListLC):
            count += 1  # Raise count

            if count > 0:  # Print invalid message
                print("Your answer was not valid.")

            userInput = input(msg)  # Grab new user input

            if not caseSensitive:  # Make lowercase if needed
                userInput = userInput.lower()

        for ans in ansList:  # Return the original answer to preserve original case
            if ans.lower() == userInput.lower():
                return ans

    def displayGame(self):
        print("\x1b[2J\x1b[H")

        for row in self.connectFour.board:
            for i in range(3):
                print("|   ", end="")
                for col in row:
                    print(*col.getRow(i), sep="  ", end="   |   ")
                print()
            print()

    def playTurn(self, player, cellPreset=None):  # Extra parameters for quick starts
        columnsPlayed = []  # Disallow same column multiple times in the same turn

        def chooseColumn(self):
            cellGame = None

            column = int(
                self.validateResponse(
                    self.connectFour.getAllColumns(columnsPlayed),
                    f"Choose a board column {player.getColoredName()}: ",
                )
            )

            for row in range(len(self.connectFour.board) - 1, 0, -1):
                if self.connectFour.board[row][column].winner == 0:
                    cellGame = self.connectFour.board[row][column]

                    return cellGame

                    break

        def chooseRow(self, cellGame):
            cellRow = None

            validAnswers = cellGame.getValidRows()

            validAnswers.append("back")

            userInput = self.validateResponse(validAnswers, "Choose a cell row: ")

            if userInput != "back":
                cellRow = int(userInput)

            else:
                return None

                newCellGame = chooseColumn(self)
                print("recursive newcell is", newCellGame)

                cellRow = chooseRow(self, newCellGame)

            return cellRow

        def chooseCol(self, cellGame, row):
            cellCol = None

            validAnswers = cellGame.getValidCols(row)

            validAnswers.append("back")

            userInput = self.validateResponse(validAnswers, "Choose a cell column: ")

            if userInput != "back":
                cellCol = int(userInput)

            else:
                return None
                newCellRow = chooseRow(self)

                cellCol = chooseCol(self, cellGame, newCellRow)

            return cellCol

        if cellPreset is None:
            cellGame = chooseColumn(self)
        else:
            cellGame = cellPreset

        cellRow = chooseRow(self, cellGame)

        if cellRow is None:
            self.playTurn(player)
            return

        cellCol = chooseCol(self, cellGame, cellRow)

        if cellCol is None:
            self.playTurn(player, cellPreset=cellGame)
            return

        cellGame.setCell(cellRow, cellCol, player)

        self.connectFour.checkWinner(player)
        self.displayGame()

        columnsPlayed.append(cellGame.id % 7)

    def playGame(self):
        self.connectFour.checkWinner(self.player1)
        self.connectFour.checkWinner(self.player2)

        while self.connectFour.winner == 0:
            for i in range(self.moves):
                if self.connectFour.winner == 0:
                    self.playTurn(self.player1)

            for i in range(self.moves):
                if self.connectFour.winner == 0:
                    self.playTurn(self.player2)

        print(f"Player {self.connectFour.winner.getColoredName()} won!")


player1 = Player(1, "Kaden", "\x1b[1;33m")
player2 = Player(2, "Nedak", "\x1b[1;31m")

e = Game(
    player1,
    player2,
)

e.displayGame()

e.playGame()
