import os, csv
from .checkingValues import Checking

class File:
    def __init__(self, name, dir):
        self.name = name
        self.dir = dir

    def createFile(self, name):
        return open(os.path.join(os.path.dirname(__name__), self, f'{name}.txt'), 'w')

    def createFileCsv(self):
        a = [['name', 'family name', 'phone']]
        with open(self, 'r', encoding='UTF-8') as m_file:
            for i in m_file:
                a.append(i.split())
        with open(os.path.join(os.path.dirname(__name__), f'{self[:-4]}.csv'), 'w') as csv_file:
            spamwriter = csv.writer(csv_file, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(a)
        return csv_file

    def deleteFile(self):
        return os.remove(self)

    def writeInF(self):
        with open(self, 'a+', encoding='UTF-8') as m_file:
            contName = Checking.checkInputStr('Enter name: ')
            contFamName = Checking.checkInputStr('Enter family name: ')
            contNumber = Checking.checkInputInt('Enter phone number: ')
            m_file.write(f"{contName} {contFamName} {contNumber}\n")
        return m_file

    def openFile(self):
        if sum(1 for line in open(self)) > 0:
            with open(self, 'r', encoding='UTF-8') as m_file:
                for i, val in enumerate(m_file):
                    print((f"{i + 1}: {val}").strip())
        else:
            print('Fail...')

    def choiseFile(self):
        return os.listdir(self)