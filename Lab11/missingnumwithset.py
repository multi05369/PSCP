'''function'''
def missingnumwithset():
    '''solution'''
    num = int(input())
    setnum1 = set(i for i in range(1, num + 1))
    setnum2 = set()
    while True:
        numcount = int(input())
        if numcount == 0:
            break
        setnum2.add(numcount)
    res = setnum1.difference(setnum2)
    res = list(res)
    res.sort()
    for i in res:
        print(i)

missingnumwithset()
