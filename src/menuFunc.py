import os
from const import DIR_PATH
from loader import check, cont, search, file, direct, comm

def menuMain():
    direct.ensureDir()
    comm.printComman(0)
    answ = comm.checkComm(check.checkInputInt(5))
    if answ == 1:
        menuLib(False, DIR_PATH)
    print('Bye!')

def menuLib(exit, dirname):
    if exit == True:
        menuMain()
    print('\nFiles: ')
    if len(os.listdir(dirname)) < 1:
        print('Not files')
        comm.printComman(1)
        answ = comm.checkComm(check.checkInputInt(5))
        if answ == 1:
            file.createFile(input('Enter file name: '))
            menuLib(False, 'LibDir')
        else:
            menuMain()
    else:
        direct.printDir()
        comm.printComman(2)
        answ = comm.checkComm(check.checkInputInt(5))
        if answ == 1:
            file.createFile(input('Enter file name: '))
            menuLib(False, DIR_PATH)
        elif answ == 2:
            while True:
                fileNum = check.checkInputInt(4)
                if fileNum <= len(os.listdir(dirname)): break
                else: print('Not find file!')
            fileName = file.choiseFile(fileNum)
            menuFail(False, fileName)
        else:
            menuMain()

def menuFail(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    print("File:")
    file.openFile(fileName, 1)
    comm.printComman(3)
    answ = comm.checkComm(check.checkInputInt(5))
    if answ == 1:
        menuContact(False, fileName)
    elif answ == 2:
        file.deleteFile(fileName)
        menuLib(False, DIR_PATH)
    elif answ == 3:
        file.createFileCsv(fileName)
        menuLib(False, DIR_PATH)
    elif answ == 4:
        comm.printComman(6)
        answ = comm.checkComm(check.checkInputInt(5))
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
        menuLib(False, DIR_PATH)

def menuContact(exit, fileName):
    if exit == True:
        menuFail(False, fileName)
    if file.openFile(fileName, 0) != 0:
        comm.printComman(5)
        answ = comm.checkComm(check.checkInputInt(5))
        if answ == 1:
            contName = check.checkInputStr(0)
            contFamName = check.checkInputStr(1)
            contNumber = check.checkInputInt(2)
            file.writeInF(fileName, contName, contFamName, contNumber)
            menuContact(False, fileName)
        elif answ == 2:
            while True:
                numStr = check.checkInputInt(6)
                if numStr <= file.openFile(fileName, 0):
                    break
                else:
                    print('Not find contact!')
            contName = check.checkInputStr(0)
            contFamName = check.checkInputStr(1)
            contNumber = check.checkInputInt(2)
            cont.updateCont(fileName, 'upd', numStr - 1, contName, contFamName, contNumber)
            menuContact(False, fileName)
        elif answ == 3:
            while True:
                numStr = check.checkInputInt(6)
                file.openFile(fileName, 1)
                if numStr <= file.openFile(fileName, 0): break
                else: print('Not find contact!')
            cont.updateCont(fileName, 'del', numStr - 1, "", "", "")
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)
    else:
        comm.printComman(4)
        answ = comm.checkComm(check.checkInputInt(5))
        if answ == 1:
            contName = check.checkInputStr(0)
            contFamName = check.checkInputStr(1)
            contNumber = check.checkInputInt(2)
            file.writeInF(fileName, contName, contFamName, contNumber)
            file.openFile(fileName, 1)
            menuContact(False, fileName)
        else:
            menuFail(False, fileName)