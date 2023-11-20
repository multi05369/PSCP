'''function'''
def difference():
    '''solution'''
    a_num = int(input())
    b_num = int(input())
    a_set = set()
    b_set = set()
    for _ in range(a_num):
        num = int(input())
        a_set.add(num)
    for _ in range(b_num):
        num2 = int(input())
        b_set.add(num2)
    res = a_set.difference(b_set)
    res = sorted(res)
    res = ' '.join(map(str, res))
    print(res)

difference()
