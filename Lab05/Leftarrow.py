'''function'''
def arrow(length, height):
    '''solution'''
    for i in range(height // 2 + 1):
        for _ in range(i, height // 2):
            print(" ", end="")
        for _ in range(length, 0, -1):
            print("*", end="")
        print()

    for i in range(height // 2, 0, -1):
        for _ in range(i - 1, height // 2):
            print(" ", end="")
        for _ in range(length):
            print("*", end="")
        print()


arrow(int(input()), int(input()))
