'''Sequence N'''
def main(num):
    '''create N'''
    for i in range(num):
        for j in range(num):
            if j == 0:
                print("*", end="")
            elif i == j:
                print("*", end="")
            elif j == num - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

main(int(input()))
