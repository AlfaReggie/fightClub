import os

def openDir():
    return os.listdir('LibDir')

def openFile(nameFile):
    if sum(1 for line in open(nameFile)) > 0:
        with open(nameFile, 'r', encoding='UTF-8') as m_file:
            for i, val in enumerate(m_file):
                print(f"{i + 1}: {val}")
    else:
        print('Fail...')