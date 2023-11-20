'''function'''
def main():
    '''solution'''
    numstart = int(input())
    numcount = int(input())
    if numstart < numcount:
        for i in range(numstart, numcount + 1, 1):
            print(i)
    else:
        for i in range(numstart, numcount - 1, -1):
            print(i)

main()
