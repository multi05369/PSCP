'''function'''
def find_sum(nnn):
    '''find sum'''
    if nnn <= 0:
        return 0
    elif nnn == 1:
        return 1
    else:
        return find_sum(nnn - 1) + find_sum(nnn - 2)

def fiborecursion(num):
    '''solution'''
    res = find_sum(num)
    print(res)
fiborecursion(int(input()))
