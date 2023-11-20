'''function'''
def coupon():
    '''solution'''
    price = float(input())
    discount1 = input().split()
    discount2 = input().split()
    paid1 = None
    paid2 = None
    if price >= float(discount1[1]):
        paid1 = price - float(discount1[0])
    if price >= float(discount2[1]):
        dis = (float(discount2[0]) / 100) * price
        paid2 = price - dis
    if paid1 is not None and paid2 is not None:
        if paid1 > paid2:
            print("2 %.1f" % max(paid2, 0))
        elif paid2 > paid1:
            print("1 %.1f" % max(paid1, 0))
        else:
            if float(discount1[1]) < float(discount2[1]):
                print("1 %.1f" % max(paid1, 0))
            elif float(discount2[1]) < float(discount1[1]):
                print("2 %.1f" % max(paid2, 0))
            else:
                print("Nope")
    elif paid1 is not None:
        print("1 %.1f" % max(paid1, 0))
    elif paid2 is not None:
        print("2 %.1f" % max(paid2, 0))
    else:
        print("Nope")

coupon()
