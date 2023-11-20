'''function'''
def stamps(rob):
    '''solution'''
    price = int(input()) #price for bill
    stamp = int(input()) #stamp get
    each_s = int(input()) #if collect equal
    discount_next = int(input()) #use stamp to discount in next time
    total = 0
    total_s = 0
    for _ in range(rob):
        times = int(input())
        if total_s >= each_s:
            check = times // discount_next
            if times % discount_next > 0:
                check += 1
            check2 = total_s // each_s
            dis_win = min(check, check2)
            if dis_win > 0:
                times -= dis_win * discount_next
                times = max(times, 0)
                total_s -= dis_win * each_s
        if times >= price:
            total_s += (times // price) * stamp
        total += times
    print(total)
    print(total_s)

stamps(int(input()))
