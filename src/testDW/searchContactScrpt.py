class Search:
    def __init__(self, nameFile):
        self.fName = nameFile

    def searchContScrpt(self, flag, searchPoint):
        with open(self) as f:
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
                    if a[2] == searchPoint:
                        return i
                    return "Not found contact!"
