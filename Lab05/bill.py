'''function'''
def bill(price):
    '''solution'''
    service = (price * 10) / 100
    if service < 50:
        service = 50
    if service > 1000:
        service = 1000
    vat = (price + service) * 7 / 100
    total = price + vat + service
    print("%.2f" % total)

bill(int(input()))
