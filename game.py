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

    def displayGame(self, boardCol=-1, cellRow=-1, cellCol=-1, step=""):
        print("\x1b[2J\x1b[H")  # Clear console

        for row in range(len(self.connectFour.board)):
            print(" " * 7, end="")

            for i in range(7):
                for j in range(3):
                    if i == cellCol and step == "cellCol":
                        if str(j) in self.connectFour.board[row][i].getValidCols(
                            cellRow
                        ):
                            print("\x1b[1;1m", end="")
                        else:
                            print("\x1b[0;2m", end="")
                    else:
                        print("\x1b[0;2m", end="")

                    print(j, end="\x1b[0;0m  ")
                print("     ", end="")

            print()

            lowestRow = self.connectFour.getLowestCell(boardCol)

            for i in range(3):
                if lowestRow == row and step == "cellRow":
                    if str(i) in self.connectFour.board[row][boardCol].getValidRows():
                        print("\x1b[1;1m", end="")
                    else:
                        print("\x1b[0;2m", end="")
                else:
                    print("\x1b[0;2m", end="")

                print(" " + str(i), end="\x1b[0;0m ")

                print("|   ", end="")  # Cell seperator

                for col in self.connectFour.board[row]:
                    print(*col.getRow(i), sep="  ", end="   |   ")
                print()

        print(" " * 10, end="")

        for i in range(7):
            if step == "boardCol":
                if self.connectFour.getColumnValidity(i):
                    print("\x1b[1;1m", end="")
                else:
                    print("\x1b[0;2m", end="")
            else:
                print("\x1b[0;2m", end="")

            print(str(i) + "\x1b[0;0m", end=" " * 13)

        print("\n")  # Empty line between board prompt

    def playTurn(self, player, cellPreset=None):  # Extra parameters for quick starts
        columnsPlayed = []  # Disallow same column multiple times in the same turn

        def chooseColumn(self):
            cellGame = None

            column = int(
                self.validateResponse(
                    self.connectFour.getAllColumns(columnsPlayed),
                    f"{player.getColoredName()} - Choose a board column: ",
                )
            )

            cellGame = self.connectFour.board[self.connectFour.getLowestCell(column)][
                column
            ]

            return cellGame

        def chooseRow(self, cellGame):
            cellRow = None

            validAnswers = cellGame.getValidRows()

            validAnswers.append("back")

            userInput = self.validateResponse(
                validAnswers, f"{player.getColoredName()} - Choose a cell row: "
            )

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

            userInput = self.validateResponse(
                validAnswers, f"{player.getColoredName()} - Choose a cell column: "
            )

            if userInput != "back":
                cellCol = int(userInput)

            else:
                return None
                newCellRow = chooseRow(self)

                cellCol = chooseCol(self, cellGame, newCellRow)

            return cellCol

        self.displayGame(step="boardCol")

        if cellPreset is None:
            cellGame = chooseColumn(self)
        else:
            cellGame = cellPreset

        column = cellGame.id % 7  # Number column

        self.displayGame(boardCol=column - 1, cellRow=1, step="cellRow")

        cellRow = chooseRow(self, cellGame)

        if cellRow is None:
            self.playTurn(player)
            return

        self.displayGame(
            cellCol=column - 1, cellRow=int(cellRow), step="cellCol"
        )  # Index, not number

        cellCol = chooseCol(self, cellGame, cellRow)

        if cellCol is None:
            self.playTurn(player, cellPreset=cellGame)
            return

        cellGame.setCell(cellRow, cellCol, player)

        self.connectFour.checkWinner(player)
        self.displayGame()

        columnsPlayed.append(column)

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
