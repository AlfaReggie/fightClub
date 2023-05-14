class Commands:

    def __init__(self, commands: list):
        self.commands = commands

    def printComman(self, numbMenu: int):
        print("\nCommands:")
        for i, co in enumerate(self.commands[numbMenu]):
            print(f"{i + 1}: {co}")

    def checkComm(self, choiseMenu: int):
        if choiseMenu > len(self.commands):
            print('Not find command!')
            return Commands.checkComm(self, choiseMenu)
        return int(choiseMenu)