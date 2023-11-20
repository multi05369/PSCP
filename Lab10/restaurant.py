'''function'''
def restaurant():
    '''solution'''
    oldprice = float(input())
    newprice = float(input())
    promotion = (100 - float(input())) / 100
    order_price = float(input())
    pricesum = oldprice + order_price
    if pricesum >= newprice:
        pricesum = pricesum * promotion
    if oldprice >= newprice:
        oldprice = oldprice * promotion
    if oldprice < pricesum:
        print("No %.3f" % (pricesum - oldprice))
    elif oldprice > pricesum:
        print("Yes %.3f" % (oldprice - pricesum))
    else:
        print("Yes")

restaurant()
