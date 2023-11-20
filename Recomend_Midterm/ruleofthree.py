'''function'''
def ruleofthree():
    '''solution'''
    num = int(input())
    price_1 = float(input())
    gram_1 = float(input())
    lowest = gram_1 / price_1
    for _ in range(num - 1):
        price_2 = float(input())
        gram_2 = float(input())
        check = gram_2 / price_2
        if check > lowest:
            lowest = check
            price_1 = price_2
            gram_1 = gram_2
        elif check == lowest:
            if price_2 < price_1:
                price_1 = price_2
                gram_1 = gram_2
    print("%.2f %.2f" %(price_1, gram_1))

ruleofthree()
