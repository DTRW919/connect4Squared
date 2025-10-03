class TicTacToe:
    def __init__(self, player1, player2, id=-1):
        self.id = id

        self.player1 = 1
        self.player2 = 2

        self.board = []
        self.empty = "0"

        self.winner = 0
        # TEST
        # winners = [1, 8, 15, 22, 29, 36]
        # if self.id in winners:
        #     if self.id % 2 == 0:
        #         self.winner = self.player1
        #     else:
        #         self.winner = self.player2
        # else:
        #     self.winner = 0

        for i in range(3):  # Rows
            self.board.append([])

            for j in range(3):  # Columns
                self.board[i].append(self.empty)

    def __str__(self):
        returnString = ""

        for row in self.board:
            returnString += " | ".join(self.board[0])
            returnString += "    "

        return returnString

    def getRow(self, row):
        if self.winner == 0:
            return self.board[row]
        elif row == 1:  # Center row
            return [" ", self.winner, " "]
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
