import re
from .checkingValues import Checking

class Contact:

    def __init__(self, file: str = "test", flag: str = "test", cont: int = "test"):
        self.file = file
        self.flag = flag
        self.cont = cont

    def updateCont(self):
        with open(self.file) as f:
            lines = f.readlines()
        delStr = lines[self.cont]
        pattern = re.compile(re.escape(delStr))
        with open(self.file, 'w') as f:
            if self.flag == 'del':
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
            elif self.flag == 'upd':
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
                    else:
                        contName = Checking.checkInputStr('Enter name: ')
                        contFamName = Checking.checkInputStr('Enter family name: ')
                        contNumber = Checking.checkInputInt('Enter phone number: ')
                        f.write((f"{contName} {contFamName} {contNumber}\n"))