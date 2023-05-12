import os

class Directory:

    def __init__(self, dirname):
        self.dir = dirname

    def ensureDir(self):
        return os.makedirs(self, exist_ok=True)
