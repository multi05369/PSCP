'''function'''
def duplicate():
    '''solution'''
    m_member = int(input())
    n_member = int(input())
    group_m = set()
    group_n = set()
    count = 0
    for _ in range(m_member):
        std_code = int(input())
        group_m.add(std_code)
    for _ in range(n_member):
        std_code2 = int(input())
        group_n.add(std_code2)
    res = group_m.intersection(group_n)
    for i in sorted(res, reverse=True):
        print(i)
        count = 1
    if count == 0:
        print("Nope")


duplicate()
