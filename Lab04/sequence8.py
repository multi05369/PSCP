'''function'''
def main():
    '''solution'''
    num = int(input())
    for i in range(1, num + 1):
        for j in range(i, num):
            print("  ", end=" ")
        for j in range(1, i + 1):
            print("%02d" % j, end=" ")
        print()

main()
