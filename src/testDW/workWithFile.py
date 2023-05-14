import os, csv

class File:

    def __init__(self, direc: str):
        self.dir = direc

    def createFile(self, name):
        return open(os.path.join(os.path.dirname(__name__), self.dir, f'{name}.txt'), 'w')

    def createFileCsv(self, name):
        a = [['name', 'family name', 'phone']]
        with open(os.path.join(os.path.dirname(__name__), self.dir, name), 'r', encoding='UTF-8') as m_file:
            for i in m_file:
                a.append(i.split())
        with open(os.path.join(os.path.dirname(__name__), self.dir, f'{name[:-4]}.csv'), 'w') as csv_file:
            spamwriter = csv.writer(csv_file, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(a)
        return csv_file

    def deleteFile(self, name):
        return os.remove(os.path.join(os.path.dirname(__name__), self.dir, name))

    def writeInF(self, nameFile, contName, contFamName, contNumber):
        with open(os.path.join(os.path.dirname(__name__), self.dir, nameFile), 'a+', encoding='UTF-8') as m_file:
            m_file.write(f"{contName} {contFamName} {contNumber}\n")
        return m_file

    def openFile(self, nameFile: str, flag):
        sumLine = 0
        if sum(1 for line in open(os.path.join(os.path.dirname(__name__), self.dir, nameFile))) > 0:
            with open(os.path.join(os.path.dirname(__name__), self.dir, nameFile), 'r', encoding='UTF-8') as m_file:
                for i, val in enumerate(m_file):
                    sumLine += 1
                    if flag == 1:
                        print((f"{i + 1}: {val}").strip())
        else:
            if flag == 1:
                print('Empty fail...')
        return sumLine


    def choiseFile(self, numbFile: int):
        return os.listdir(self.dir)[numbFile - 1]
