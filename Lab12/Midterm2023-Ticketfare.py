'''function'''
def ticket():
    '''solution'''
    n_station = int(input())
    a_station = int(input())
    b_baht = int(input())
    c_station = int(input())
    d_baht = int(input())
    e_baht = int(input())
    f_start = int(input())
    g_end = int(input())
    station = abs(f_start - g_end)

    if findmaax(f_start, g_end) > n_station:
        return "Error"

    res = b_baht \
        + findmaax(0, findmiin(c_station, station - a_station)) * d_baht \
        + findmaax(0, station - c_station - a_station) * e_baht
    return res

def findmaax(num1, num2):
    '''find maax'''
    return num1 if num1 > num2 else num2

def findmiin(num1, num2):
    '''find miin'''
    return num1 if num1 < num2 else num2

print(ticket())
