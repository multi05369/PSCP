'''function'''
def rungame():
    '''solution'''
    items = input().split()
    run = 0
    before = 0
    for i in items:
        run += abs(int(i) - before)
        before = int(i)
    print(run)

rungame()
