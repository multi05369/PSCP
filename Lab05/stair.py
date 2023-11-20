'''function'''
def stair():
    '''solution'''
    pace = int(input())
    num = int(input())
    step = 0
    count = 0
    can = True
    for _ in range(1, num+1):
        step_up = int(input())
        step += step_up
        if step_up > pace:
            can = False
        elif step == pace:
            count += 1
            step = 0
        elif step > pace:
            count += 1
            step = step_up
    if step > 0:
        count += 1
    if can:
        print(count)
    else:
        print("NO")

stair()
