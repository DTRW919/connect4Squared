from ticTacToe import TicTacToe


class ConnectFour:
    def __init__(self, player1, player2):
        self.board = []

        self.player1 = player1
        self.player2 = player2

        self.winner = 0

        for i in range(6):  # Rows
            self.board.append([])

            for j in range(7):  # Columns
                self.board[i].append(TicTacToe(player1, player2, 7 * i + j + 1))

    def printBoard(self):
        for row in self.board:
            print(*row, sep="  ")

    def setSquare(self, column, player):
        for row in self.board[::-1]:
            if row[column].winner == 0:
                if player == 1:
                    row[column] = self.player1
                else:
                    row[column] = self.player2
                break

        # Return False if unable to fill column
        return False

    def getColumnValidity(self, column):  # Whether a column can still be played
        validCells = 0

        for row in self.board:
            if row[column].winner == 0:
                validCells += 1

        return validCells

    def getAllColumns(self):  # Get all columns that are playable
        validColumns = []

        for column in range(len(self.board[0])):
            if self.getColumnValidity(column) > 0:
                validColumns.append(str(column))

        return validColumns

    def checkWinner(self, player):
        # Column
        for row in range(len(self.board) - 4):
            for column in range(len(self.board[0])):
                if self.board[row][column].winner == player:
                    if self.board[row][column + 1].winner == player:
                        if self.board[row][column + 2].winner == player:
                            if self.board[row][column + 3].winner == player:
                                self.winner = player

        # Rows
        for row in range(len(self.board[0]) - 4):
            for column in range(len(self.board)):
                if self.board[row][column].winner == player:
                    if self.board[row + 1][column].winner == player:
                        if self.board[row + 2][column].winner == player:
                            if self.board[row + 3][column].winner == player:
                                self.winner = player

        # Diagonal Ascending
        for row in range(2, len(self.board[0])):
            row -= 1
            for column in range(len(self.board) - 4):
                if self.board[row][column].winner == player:
                    if self.board[row - 1][column + 1].winner == player:
                        if self.board[row - 2][column + 2].winner == player:
                            if self.board[row - 3][column + 3].winner == player:
                                self.winner = player

        # Diagonal Descending
        for row in range(2, len(self.board[0])):
            row -= 1
            for column in range(3, len(self.board)):
                if self.board[row][column].winner == player:
                    if self.board[row - 1][column - 1].winner == player:
                        if self.board[row - 2][column - 2].winner == player:
                            if self.board[row - 3][column - 3].winner == player:
                                self.winner = player
