class Search:

    def __init__(self, nameFile: str = "test", flag: str = "test", searchPoint: str = "test"):
        self.fName = nameFile
        self.flag = flag
        self.searchPoint = searchPoint

    def searchContScrpt(self):
        with open(self.fName) as f:
            for i in f:
                a = list(i.split())
                if self.flag == 'frstName':
                    if a[0] == self.searchPoint:
                        return i
                    return "Not found contact!"
                elif self.flag == 'famName':
                    if a[0] == self.searchPoint:
                        return i
                    return "Not found contact!"
                elif self.flag == 'phone':
                    if a[2] == int(self.searchPoint):
                        return i
                    return "Not found contact!"
