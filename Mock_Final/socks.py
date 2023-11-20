'''function'''
def socks(text):
    '''solution'''
    socksort = ''
    socklist = []
    count = 0
    for i in sorted(text):
        socksort += i
    for i in range(len(socksort) - 1):
        if socksort[i] == socksort[i + 1]:
            socklist.append(str(socksort[i] + str(socksort[i + 1]))
            count = 1
            i += 1
    if count == 1:
        print(' '.join(socklist))
    else:
        print("None")
    print(len(socklist))

socks(input().upper())
