import os

class Directory:

    def __init__(self, nameDir):
        self.dir = nameDir

    def ensureDir(self):
        return os.makedirs(self.dir, exist_ok=True)

    def printDir(self):
        for i, file in enumerate(os.listdir(self.dir)):
            print(f"{i + 1} - {file}")
