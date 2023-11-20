'''function'''
def shorten():
    '''solution'''
    res = ""
    start = None
    previous = None
    while True:
        num = int(input())
        if num == -1:
            break

        if start == None:
            start = num
            previous = num
            continue
        else:
            if previous != num - 1:
                if start == previous:
                    res += "%d, " % start
                else:
                    res += "%d-%d, " % (start, previous)
                start = num
                previous = num
            else:
                previous = num
    if start != None:
        if start == previous:
            res += "%d, " % start
        else:
            res += "%d-%d, " % (start, previous)
    print(res.strip(", "))

shorten()
