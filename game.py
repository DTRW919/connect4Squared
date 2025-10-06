from connectFour import ConnectFour
from player import Player


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.turns = 2

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

    def playTurn(self, player):
        columnsPlayed = []

        for i in range(self.turns):
            column = int(
                self.validateResponse(
                    self.connectFour.getAllColumns(columnsPlayed),
                    f"Choose a column player {player.getColoredName()}: ",
                )
            )

            for row in range(len(self.connectFour.board) - 1, 0, -1):
                if self.connectFour.board[row][column].winner == 0:
                    cellGame = self.connectFour.board[row][column]

                    break

            cellRow = int(
                self.validateResponse(cellGame.getValidRows(), "Choose a cell row: ")
            )

            cellCol = int(
                self.validateResponse(
                    cellGame.getValidCols(cellRow), "Choose a cell column: "
                )
            )

            cellGame.setCell(cellRow, cellCol, player)

            self.connectFour.checkWinner(player)
            self.displayGame()

            columnsPlayed.append(column)

    def playGame(self):
        self.connectFour.checkWinner(self.player1)
        self.connectFour.checkWinner(self.player2)

        while self.connectFour.winner == 0:
            self.playTurn(self.player1)

            if self.connectFour.winner == 0:
                self.playTurn(self.player2)

        print(f"Player {self.connectFour.winner} won!")


player1 = Player(1, "Kaden", "\x1b[1;33m")
player2 = Player(2, "Nedak", "\x1b[1;31m")

e = Game(
    player1,
    player2,
)

e.displayGame()

e.playGame()
