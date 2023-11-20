'''christmas tree'''
def christmas(tree, cone):
    '''solution'''
    for i in range(1, tree + 1):
        for _ in range(i, tree):
            print(" ", end="")
        for _ in range(i - 1):
            print("*", end="")
        for _ in range(i, 0, -1):
            print("*", end="")
        print()

    for _ in range(cone):
        print(" " * (tree - 2), end="")
        print("---", end="")
        print()

christmas(int(input()), int(input()))
