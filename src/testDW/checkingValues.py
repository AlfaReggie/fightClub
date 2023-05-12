class Checking:

    def __init__(self, val):
        self.val = val

    def checkInputStr(self):
        checkNum = input(self)
        if checkNum.replace("-", '').isalpha():
            return checkNum
        print("Error!")
        return Checking.checkInputStr(f'{self}')


    def checkInputInt(self):
        checkNum = input(self)
        if checkNum.replace("-", '').isdigit():
            if int(checkNum) < 0:
                print("Error! Can't negative!")
                return Checking.checkInputInt(f'{self}')
            return int(checkNum)
        print("Error!")
        return Checking.checkInputInt(f'{self}')


    def checkComm(self):
        userAnsw = Checking.checkInputInt('\nSelect command:')
        if userAnsw > self:
            print('Not find command!')
            return Checking.checkComm(self)
        return int(userAnsw)