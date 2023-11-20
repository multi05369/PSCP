'''function'''
def saintseiya():
    '''solution'''
    second = int(input())
    punch = int(input())
    punch_all = 0
    for i in range(2, second + 1, 2):
        if punch_all < punch:
            if i % 6 == 0:
                punch_all += 1
            elif i % 2 == 0:
                punch_all += 165
        else:
            punch_all += (second + 1 - i) * 12
            break
    print(punch_all)

saintseiya()
