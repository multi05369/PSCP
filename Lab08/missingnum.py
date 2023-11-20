'''function'''
def missingnumber(num):
    '''solution'''
    listnum = []
    while True:
        numcount = int(input())
        listnum.append(numcount)
        if numcount == 0:
            break
    listnum.sort()
    for i in range(num + 1):
        if i not in listnum:
            print(i)

missingnumber(int(input()))
