'''function'''
def main():
    '''solution'''
    aaa = int(input()) #5
    bbb = int(input()) #3
    ccc = int(input()) #1
    ddd = int(input()) #8

    box_donut = bbb + ccc #3 + 1 = 4
    price_box = aaa*bbb #5 * 3 = 15
    num_box = ddd // box_donut #8 // 4 = 2
    remaining = ddd - (num_box * box_donut) #8 - (2 * 4)
    if remaining >= bbb: #0 >= 3 False
        num_box = num_box + 1
        remaining = 0
    price = num_box * price_box + remaining * aaa #2 * 15 + 0 * 5
    donut = num_box * box_donut + remaining #2 * 4 + 0
    print("%d ชิ้น" % donut)
    print("%d บาท" % price)

main()
