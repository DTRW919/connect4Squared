class Player:
    def __init__(self, id, name, color):
        self.id = id

        self.name = name

        self.color = color

    def getName(self, length=999):
        return self.name[0:length]

    def getColoredName(self, length=999):
        return self.color + self.name[0:length] + "\x1b[1;0m"
