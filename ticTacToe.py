class TicTacToe:
    def __init__(self, player1, player2, id=-1):
        self.id = id

        self.player1 = player1
        self.player2 = player2

        self.board = []
        self.empty = "•"

        self.winner = 0
        # TEST
        # winners = [38]
        # if self.id in winners:
        #     self.winner = self.player1
        # else:
        #     self.winner = 0

        for i in range(3):  # Rows
            self.board.append([])

            for j in range(3):  # Columns
                self.board[i].append(self.empty)

    def getRow(self, row):
        if self.winner == 0 or self.winner == -1:
            returnRow = list(self.board[row])

            for space in range(len(returnRow)):
                if returnRow[space] == self.player1:
                    returnRow[space] = self.player1.getColoredName(1)
                elif returnRow[space] == self.player2:
                    returnRow[space] = self.player2.getColoredName(1)

            return returnRow

        elif row == 1:  # Center row because someone won
            if self.winner == self.player1:
                return [" ", self.player1.getColoredName(1) + "\x1b[1;0m", " "]
            else:
                return [" ", self.player2.getColoredName(1) + "\x1b[1;0m", " "]
        else:
            return [" ", " ", " "]

    def getValidRows(self):
        validRows = []

        for row in range(len(self.board)):
            if self.empty in self.board[row]:
                validRows.append(str(row))

        return validRows

    def getValidCols(self, row):
        validColumns = []

        for column in range(len(self.board)):
            if self.board[row][column] is self.empty:
                validColumns.append(str(column))

        return validColumns

    def printBoard(self):
        for row in self.board:
            print(*row, sep="  ")

    def getCell(self, row, column):
        return self.board[row][column]

    def setCell(self, row, column, player):
        if self.board[row][column] == self.empty:
            self.board[row][column] = player

        if self.checkWinner(player):
            self.winner = player
        else:
            self.checkTie()

    def checkTie(self):
        for row in self.board:
            if self.empty in row:
                return

        self.winner = -1

    def checkWinner(self, player):
        # Rows
        for row in self.board:
            if (
                len(set(row)) == 1 and row[0] == player
            ):  # No duplicates meaning all the same AND is player
                return True

        # Columns
        for i in range(3):
            column = []

            for row in self.board:
                column.append(row[i])

            if len(set(column)) == 1 and column[0] == player:
                return True

        # Diagonal Ascending
        if self.board[0][2] == player:
            if self.board[1][1] == player:
                if self.board[2][0] == player:
                    return True

        # Diagonal Descending
        if self.board[0][0] == player:
            if self.board[1][1] == player:
                if self.board[2][2] == player:
                    return True

        return False
