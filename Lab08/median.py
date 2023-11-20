'''function'''
def median():
    '''solution'''
    num = int(input())
    numlist = []
    for _ in range(num):
        val = int(input())
        numlist.append(val)
    sort_numlist = sorted(numlist)
    middle = len(sort_numlist) // 2
    if len(sort_numlist) % 2 == 1:
        print("%.1f" % sort_numlist[middle])
    else:
        print("%.1f" % ((((sort_numlist[middle - 1]) + (sort_numlist[middle])) / 2.0)))
median()
