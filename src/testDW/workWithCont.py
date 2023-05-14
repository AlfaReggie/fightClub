import re, os

class Contact:

    def __init__(self, dir: str):
        self.dir = dir

    def updateCont(self, nameFile, flag, contNum, contName, contFamName, contNumber):
        with open(os.path.join(os.path.dirname(__name__), self.dir, nameFile)) as f:
            lines = f.readlines()
        delStr = lines[contNum]
        pattern = re.compile(re.escape(delStr))

        with open(os.path.join(os.path.dirname(__name__), self.dir, nameFile), 'w') as f:
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
                        f.write((f"{contName} {contFamName} {contNumber}\n"))