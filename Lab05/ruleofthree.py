'''function'''
def three(num):
    '''rule of three'''
    check = 0
    for _ in range(num):
        price = float(input())
        gram = float(input())
        res = gram / price
        if res > 0:

three(int(input()))
