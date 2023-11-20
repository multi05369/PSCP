'''function'''
def main():
    '''solution'''
    num = int(input())
    count = 0
    for _ in range(1, num + 1):
        for j in range(1, num + 1):
            print(j + count, end=" ")
        print()
        count += num

main()
