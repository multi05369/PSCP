'''function'''
def tax(year, ccc):
    '''solution'''
    price = 0
    if ccc > 1800:
        price += (ccc - 1800) * 4
        ccc = 1800
    if ccc > 600:
        price += (ccc - 600) *1.50
        ccc = 600
    price += ccc * 0.5

    if year == 6:
        price = price - (price * (10 / 100))
    elif year == 7:
        price = price - (price * (20 / 100))
    elif year == 8:
        price = price - (price * (30 / 100))
    elif year == 9:
        price = price - (price * (40 / 100))
    elif year >= 10:
        price = price - (price * (50 / 100))
    print("%.2f" % price)

tax(int(input()), int(input()))
