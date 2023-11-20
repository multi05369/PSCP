'''function'''
def sequence(num):
    '''create pattern'''
    for i in range(-num + 1, num):
        for j in range(-num + 1, num):
            print("%02d" % (num - abs(abs(i) - abs(j))), end=" ")
        print()

sequence(int(input()))
