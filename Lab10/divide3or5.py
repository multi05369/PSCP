'''function'''
def divideandsum(num):
    '''solution'''
    res = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    print(res)

divideandsum(int(input()))
