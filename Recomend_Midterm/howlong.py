'''function'''
def howlong():
    '''solution'''
    num = int(input())
    coun = 0
    if num >= 0:
        num = str(num)
        for _ in num:
            coun += 1
    elif num < 0:
        num = str(num)
        num = num.replace("-", "")
        for _ in num:
            coun += 1
    print((coun))

howlong()
