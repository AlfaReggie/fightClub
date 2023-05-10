import os

from .checkingValues import checkInputStr, checkInputInt

def ensureDir(dirname):
    return os.makedirs(dirname, exist_ok=True)

def createFile(nameFile, dirName):
    return open(os.path.join(os.path.dirname(__name__), dirName, f'{nameFile}.txt'), 'w')

def createFileCsv(nameFile):
    return open(os.path.join(os.path.dirname(__name__), f'{nameFile[:-4]}.csv'), 'w')

def deleteFile(fileName):
    return os.remove(fileName)

def writeInF(nameFile):
    with open(nameFile, 'a+', encoding='UTF-8') as m_file:
        contName = checkInputStr('Enter name: ')
        contFamName = checkInputStr('Enter family name: ')
        contNumber = checkInputInt('Enter phone number: ')
        m_file.write(f"{contName} {contFamName} {contNumber}\n")
    return m_file