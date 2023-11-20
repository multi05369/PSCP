'''function'''
import math
def books():
    '''solution'''
    book = int(input())
    page = int(input())
    xxx = int(input())
    yyy = int(input())
    count = 0
    day = 0
    numpage = 0
    while True:
        read = math.ceil((xxx / yyy) * page)
        if count == book:
            break
        if read >= page:
            break
        numpage += read
        if numpage >= page:
            count += 1
            numpage = 0
        xxx += 1
        yyy += 1
        day += 1
    day += book - count
    print(day)

books()
