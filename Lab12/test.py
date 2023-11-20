'''function'''
def coke():
    '''solution'''
    aaa = int(input()) #bottle
    bbb = int(input()) #bottle_cap
    ccc = int(input()) #new_price
    ddd = int(input()) #bottle_want
    money = 0
    count = 0
    while ddd:
        if count == bbb:
            if bbb == 0:
                money += aaa
            else:
                money += ccc
                count = 0
        else:
            money += aaa
        count += 1
        ddd -= 1
    print(money)

coke()
