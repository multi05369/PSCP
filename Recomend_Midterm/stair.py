'''function'''
def stair():
    '''solution'''
    pace = int(input())
    num = int(input())
    walk = 0
    can_not = 0
    count = 0
    for _ in range(num):
        step = int(input())
        count = step + count
        if step > pace:
            can_not += 1
        elif count == pace:
            walk += 1
            count = 0
        elif count > step:
            walk += 1
            count = step
    if count > 0:
        walk += 1
    if can_not == 1:
        print("NO")
    else:
        print(walk)

stair()
