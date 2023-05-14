import os

class Search:

    def __init__(self, dir: str):
        self.dir = dir

    def searchContScrpt(self, fName, flag, searchPoint):
        with open(os.path.join(os.path.dirname(__name__), self.dir, fName)) as f:
            for i in f:
                a = list(i.split())
                if flag == 'frstName':
                    if a[0] == searchPoint:
                        return i
                    return "Not found contact!"
                elif flag == 'famName':
                    if a[0] == searchPoint:
                        return i
                    return "Not found contact!"
                elif flag == 'phone':
                    if a[2] == int(searchPoint):
                        return i
                    return "Not found contact!"
