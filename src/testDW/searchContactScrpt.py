def searchContScrpt(file, flag, searchPoint):
    with open(file) as f:
        for i in f:
            a = list(i.split())
            if flag == 'frstName':
                if a[0] == searchPoint:
                    print(i)
            elif flag == 'famName':
                if a[0] == searchPoint:
                    print(i)
            elif flag == 'phone':
                if a[2] == searchPoint:
                    print(i)
