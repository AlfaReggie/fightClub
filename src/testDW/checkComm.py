from checkingValues import Checking

chk = Checking()

class Commands:

    def __init__(self, countComm: int = 0, message: str = "Enter number command: "):
        self.countComm = countComm
        self.message = message

    def checkComm(self):
        userAnsw = chk.checkInputInt(self.message)
        if userAnsw > self.countComm:
            print('Not find command!')
            return Commands.checkComm(self.message)
        return int(userAnsw)