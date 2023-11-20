'''function'''
def palindrome():
    '''solution'''
    num = int(input())
    time = input()
    for _ in range(num):
        if len(time) == 5:
            n = time[0]
            h = time[1]
            m = time[-2]
            j = time[-1]
            while time[1:] != time[-1:]:
                n += int(n)
                h += int(h)
                m += int(m)
                j += int(j)
                if n == 2:
                    n = 0
                if h == 9:
                    h = 0
                if m == 9:
                    m = 0
                if j == 9:
                    j = 0
                n += 1
                h += 1
                m += 1
                j += 1
            print(time)
        else:
            h = time[0]
            m = time[-2]
            j = time[-1]
            while time[1:] != time[-1:]:
                h += int(h)
                m += int(m)
                j += int(j)
                if h == 9:
                    h = 0
                if m == 9:
                    m = 0
                if j == 9:
                    j = 0
                h += 1
                m += 1
                j += 1
            print(time)

palindrome()
