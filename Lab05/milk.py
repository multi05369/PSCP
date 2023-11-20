'''milk'''
def milk():
    '''solution'''
    price_bottle = int(input())
    bottle_cap = int(input())
    free_milk = int(input())
    money = int(input())

    if bottle_cap == 0:
        milk_get = money // price_bottle
        total = milk_get
    else:
        milk_get = money // price_bottle
        free_get = (milk_get // bottle_cap) * free_milk
        total = milk_get + free_get
        remain = free_get + (milk_get % bottle_cap)
        while remain >= bottle_cap:
            free_get = (remain // bottle_cap) * free_milk
            total += free_get
            remain = free_get + (remain % bottle_cap)
    print(total)

milk()
