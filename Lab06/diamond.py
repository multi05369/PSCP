'''function'''
def diamond():
    '''solution'''
    num = int(input())
    half = num // 2
    for i in range(num):
        for j in range(num):
            if i == half or i + j == half or i - j == half or \
                num - i + half - 1 == j or j - i == half:
                print("*", end="")
            else:
                print(" ", end="")
        print()

diamond()
