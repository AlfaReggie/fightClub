import re
from .checkingValues import Checking

class Contact:

    def __init__(self, cont):
        self.cont = cont

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
                        contName = Checking.checkInputStr('Enter name: ')
                        contFamName = Checking.checkInputStr('Enter family name: ')
                        contNumber = Checking.checkInputInt('Enter phone number: ')
                        f.write((f"{contName} {contFamName} {contNumber}\n"))