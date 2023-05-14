class Checking:

    def __init__(self, val: object = "test"):
        self.val = val

    def checkInputStr(self):
        checkNum = input(self.val)
        if checkNum.replace("-", '').isalpha():
            return checkNum
        print("Error!")
        return Checking.checkInputStr(self)


    def checkInputInt(self):
        checkNum = input(self.val)
        if checkNum.replace("-", '').isdigit():
            if int(checkNum) < 0:
                print("Error! Can't negative!")
                return Checking.checkInputInt(self)
            return int(checkNum)
        print("Error!")
        return Checking.checkInputInt(self)
