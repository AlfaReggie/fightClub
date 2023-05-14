import os
from const import DIR_PATH
from loader import check, cont, search, file, direct

def choiseCommand(flag):
    comandMain = ["Open libraris", "Stop program"]
    comandLibrZero = ['Create new file', "Exit to main"]
    comandLibr = ['Create new file', "Choise file", "Exit to main"]
    comandFile = ["Update file", 'Delete file', "Save in CSV", 'Search contact', "Exit to library"]
    comandContZero = ["Add contact", 'Exit to files']
    comandContact = ["Add contact", "Update contacts", 'Delete contacts', 'Exit to files']
    comandFind = ['Search on first name', 'Search on family name', 'Search on phone', 'Exit to contact menu']
    lstCmd = [comandMain, comandLibr, comandLibrZero, comandFile, comandContZero, comandContact, comandFind]
    print('\nCommands: ')
    for i, val in enumerate(lstCmd[flag]):
        print(f"{i + 1}: {val}")
    return len(lstCmd[flag])

def menuMain():
    direct.ensureDir(DIR_PATH)
    answ = check.checkComm(choiseCommand(0))
    if answ == 1:
        menuLib(False, DIR_PATH)
    print('Bye!')

def menuLib(exit, dirname):
    if exit == True:
        menuMain()
    print('Files: ')
    if len(os.listdir(dirname)) < 1:
        print('Not files')
        answ = check.checkComm(choiseCommand(2))
        if answ == 1:
            file.createFile(DIR_PATH, input('Enter file name: '))
            menuLib(False, 'LibDir')
        else:
            menuMain()
    else:
        for i, val in enumerate(os.listdir(dirname)):
            print(f"{i + 1} - {val}")
        answ = check.checkComm(choiseCommand(1))
        if answ == 1:
            file.createFile(DIR_PATH, input('Enter file name: '))
            menuLib(False, DIR_PATH)
        elif answ == 2:
            while True:
                fileNum = check.checkInputInt('Enter number file: ')
                if fileNum <= len(os.listdir(dirname)): break
                else: print('Not find file!')
            fileName = f"LibDir/{file.choiseFile(DIR_PATH)[fileNum - 1]}"
            menuFail(False, fileName)
        else:
            menuMain()

def menuFail(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    print("File:")
    file.openFile(fileName)
    answ = check.checkComm(choiseCommand(3))
    if answ == 1:
        menuContact(False, fileName)
    elif answ == 2:
        file.deleteFile(fileName)
        menuLib(False, DIR_PATH)
    elif answ == 3:
        file.createFileCsv(fileName)
        menuLib(False, DIR_PATH)
    elif answ == 4:
        answ = check.checkComm(choiseCommand(6))
        if answ == 1:
            searchPnt = input('Enter first name: ')
            print(search.searchContScrpt(fileName, 'frstName', searchPnt))
        elif answ == 2:
            searchPnt = input('Enter family name: ')
            print(search.searchContScrpt(fileName, 'famName', searchPnt))
        elif answ == 3:
            searchPnt = input('Enter phone: ')
            print(search.searchContScrpt(fileName, 'phone', searchPnt))
        else:
            menuFail(True, fileName)
        menuFail(True, fileName)
    else:
        menuLib(False, 'LibDir')

def menuContact(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    if sum(1 for line in open(fileName)) != 0:
        answ = check.checkComm(choiseCommand(5))
        if answ == 1:
            file.writeInF(fileName)
            file.openFile(fileName)
            menuContact(False, fileName)
        elif answ == 2:
            file.openFile(fileName)
            while True:
                numStr = check.checkInputInt("Select contact: ")
                if numStr <= sum(1 for line in open(fileName)): break
                else: print('Not find contact!')
            cont.updateCont(fileName, numStr - 1, 'upd')
            menuContact(False, fileName)
        elif answ == 3:
            file.openFile(fileName)
            while True:
                numStr = check.checkInputInt("Select contact: ")
                if numStr <= sum(1 for line in open(fileName)): break
                else: print('Not find contact!')
            cont.updateCont(fileName, numStr - 1, 'del')
            file.openFile(fileName)
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)
    else:
        choiseCommand(5)
        userAnswCont = check.checkInputInt('\nSelect command:')
        if userAnswCont == 1:
            file.writeInF(fileName)
            file.openFile(fileName)
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)