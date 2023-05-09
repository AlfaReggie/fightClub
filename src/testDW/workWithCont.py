from src.testDW import *
import re

def updateCont(file, numCont, flag):
    with open(file) as f:
        lines = f.readlines()
    delStr = lines[numCont]
    pattern = re.compile(re.escape(delStr))
    with open(file, 'w') as f:
        if flag == 'del':
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    f.write(line)
        elif flag == 'upd':
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    f.write(line)
                else:
                    contName = checkInputStr('Enter name: ')
                    contFamName = checkInputStr('Enter family name: ')
                    contNumber = checkInputInt('Enter phone number: ')
                    f.write((f"{contName} {contFamName} {contNumber}\n"))