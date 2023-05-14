class Checking:

    def __init__(self, val: list):
        self.val = val

    def checkInputStr(self, numVal: int):
        checkNum = input(f"Enter {self.val[numVal]}: ")
        if checkNum.replace("-", '').isalpha():
            return checkNum
        print("Error!")
        return Checking.checkInputStr(self, numVal)


    def checkInputInt(self, numbStrVal: int):
        checkNum = input(f"\nEnter {self.val[numbStrVal]}: ")
        if checkNum.replace("-", '').isdigit():
            if int(checkNum) < 0:
                print("Error! Can't negative!")
                return Checking.checkInputInt(self)
            return int(checkNum)
        print("Error!")
        return Checking.checkInputInt(self)
