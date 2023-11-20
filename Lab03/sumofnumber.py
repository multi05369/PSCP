'''function'''
def main():
    '''solution'''
    score = abs(int(input()))
    count = 0
    while True:
        num = int(input())
        if num == -1:
            break
        count += num
        if count == score:
            break
    print(count)

main()
