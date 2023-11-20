'''function'''
def sequence(num):
    '''create sequence'''
    for i in range(-num + 1, num):
        for j in range(-num + 1, num):
            res = abs(i) + abs(j) + 1
        if res > num:
            res = 2 * num - res
            print("%02d" % res, end=" ")
        for j in range(1, i):
            res = abs(i) + abs(j) + 1
        if res == num:
            res = 2 * num - res
            print("%02d" % res, end=" ")
        for j in range(num, 0, -1):
            res = abs(i) + abs(j) + 1
        if res < num:
            res = 2 * num - res
            print("%02d" % res, end=" ")
        print()
sequence(int(input()))
