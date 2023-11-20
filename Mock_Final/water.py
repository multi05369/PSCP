'''function'''
def water():
    '''solution'''
    month = int(input())
    price_water = float(input())
    over_use = float(input()) #water that over use
    newprice = float(input())
    notover = float(input())
    res = 0
    for _ in range(month):
        water_use = float(input())
        if water_use < over_use:
            water_use = water_use * price_water
            if water_use <= notover:
                res += 0
            else:
                res += water_use
        else:
            diff = abs(water_use - over_use)
            after_diff = water_use - diff
            new_bill = newprice * diff
            res2 = (after_diff * price_water) + (new_bill)
            if res2 <= notover:
                res2 = 0
                res += res2
            else:
                res += res2
    print("%.2f" % res)

water()
