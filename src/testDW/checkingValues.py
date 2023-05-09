def checkInputStr(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isalpha():
        return checkNum
    else:
        print("Error!")
        return checkInputStr(f'{message}')

def checkInputInt(message: str) -> int:
    checkNum = input(message)
    if checkNum.replace("-", '').isdigit():
        if int(checkNum) < 0:
            print("Error! Can't negative!")
            return checkInputInt(f'{message}')
        return int(checkNum)
    else:
        print("Error!")
        return checkInputInt(f'{message}')

def checkComm(flag):
    userAnsw = checkInputInt('\nSelect command:')
    if userAnsw > flag:
        print('Not find command!')
        return checkComm(flag)
    else:
        return int(userAnsw)