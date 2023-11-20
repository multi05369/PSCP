'''funciton'''
def homerun(num):
    '''solution'''
    hit_lenght = float(input())
    count = 0
    for _ in range(num):
        area = float(input())
        if hit_lenght > area:
            count += 1
    print(count)

homerun(int(input()))
