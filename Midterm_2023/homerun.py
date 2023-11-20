'''function'''
def homerun():
    '''solution'''
    num = int(input())
    hit_range = float(input())
    hit = 0
    for _ in range(num):
        area = float(input())
        if hit_range > area:
            hit += 1
    print(hit)

homerun()
