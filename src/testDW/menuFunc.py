import os, csv
from src.testDW import *
from src.testDW.workWithCont import updateCont
from src.testDW.searchContactScrpt import searchContScrpt

def choiseCommand(flag):
    comandMain = ["Open libraris", "Stop program"]
    comandLibrZero = ['Create new file', "Exit to main"]
    comandLibr = ['Create new file', "Choise file", "Exit to main"]
    comandFile = ["Update file", 'Delete file', "123", 'Search contact', "Exit to library"]
    comandContZero = ["Add contact", 'Exit to files']
    comandContact = ["Add contact", "Update contacts", 'Delete contacts', 'Exit to files']
    comandFind = ['Search on first name', 'Search on family name', 'Search on phone', 'Exit to contact menu']
    lstCmd = [comandMain, comandLibr, comandLibrZero, comandFile, comandContZero, comandContact, comandFind]
    print('\nCommands: ')
    for i, val in enumerate(lstCmd[flag]):
        print(f"{i + 1}: {val}")
    return len(lstCmd[flag])

def menuMain():
    ensureDir('LibDir')
    answ = checkComm(choiseCommand(0))
    if answ == 1:
        menuLib(False, 'LibDir')
    else:
        print('Bye!')

def menuLib(exit, dirname):
    if exit == True:
        menuMain()
    print('Files: ')
    if len(os.listdir(dirname)) < 1:
        print('Not files')
        answ = checkComm(choiseCommand(2))
        if answ == 1:
            createFile(input('Enter file name: '), 'LibDir')
            menuLib(False, 'LibDir')
        else:
            menuMain()
    else:
        for i, val in enumerate(os.listdir(dirname)):
            print(f"{i + 1} - {val}")
        answ = checkComm(choiseCommand(1))
        if answ == 1:
            createFile(input('Enter file name: '), 'LibDir')
            menuLib(False, 'LibDir')
        elif answ == 2:
            while True:
                fileNum = checkInputInt('Enter number file: ')
                if fileNum <= len(os.listdir(dirname)): break
                else: print('Not find file!')
            fileName = f"LibDir/{openDir()[fileNum - 1]}"
            menuFail(False, fileName)
        else:
            menuMain()

def menuFail(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    openFile(fileName)
    answ = checkComm(choiseCommand(3))
    if answ == 1:
        menuContact(False, fileName)
    elif answ == 2:
        deleteFile(fileName)
        menuLib(False, 'LibDir')
    elif answ == 3:
        pass
    elif answ == 4:
        answ = checkComm(choiseCommand(6))
        if answ == 1:
            searchPnt = input('Enter first name: ')
            searchContScrpt(fileName, 'frstName', searchPnt)
        elif answ == 2:
            searchPnt = input('Enter family name: ')
            searchContScrpt(fileName, 'famName', searchPnt)
        elif answ == 3:
            searchPnt = input('Enter phone: ')
            searchContScrpt(fileName, 'phone', searchPnt)
        else:
            menuFail(True, fileName)
        menuFail(True, fileName)

    else:
        menuLib(False, 'LibDir')

def menuContact(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    if sum(1 for line in open(fileName)) != 0:
        answ = checkComm(choiseCommand(5))
        if answ == 1:
            writeInF(fileName)
            openFile(fileName)
            menuContact(False, fileName)
        elif answ == 2:
            openFile(fileName)
            while True:
                numStr = checkInputInt("Select contact: ")
                if numStr <= sum(1 for line in open(fileName)): break
                else: print('Not find contact!')
            updateCont(fileName, numStr - 1, 'upd')
            menuContact(False, fileName)
        elif answ == 3:
            openFile(fileName)
            while True:
                numStr = checkInputInt("Select contact: ")
                if numStr <= sum(1 for line in open(fileName)): break
                else: print('Not find contact!')
            updateCont(fileName, numStr - 1, 'del')
            openFile(fileName)
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)
    else:
        choiseCommand(5)
        userAnswCont = checkInputInt('\nSelect command:')
        if userAnswCont == 1:
            writeInF(fileName)
            openFile(fileName)
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)