'''function'''
def sequence(num):
    '''create pattern'''
    for i in range(-num + 1, num):
        for j in range(-num + 1, num):
            result = max(abs(i), abs(j))
            print("%02d" % (num - result), end=" ")
        print()

sequence(int(input()))
