import os

class Directory:

    def __init__(self, dir_path):
        self.dir = dir_path

    def ensureDir(self):
        return os.makedirs(self.dir, exist_ok=True)
