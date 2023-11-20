'''function'''
def tuplesad():
    '''solution'''
    val = tuple(input().split())
    position = input()
    pos = val.index(position)
    amount = val.count(position)
    for _ in range(amount):
        for _ in range(amount):
            print(pos, end=" ")
        print()

tuplesad()
