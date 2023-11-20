'''function'''
def area():
    '''solution'''
    num = int(input())
    block = 0
    for _ in range(num):
        lines = input().replace(" ", "")
        block += len(lines)
    print(block)

area()
