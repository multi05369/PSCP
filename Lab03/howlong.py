'''function'''
def main():
    '''solution'''
    result = 0
    num = int(input())
    if num >= 0:
        num = str(num)
        for _ in num:
            result += 1
        print(result)

    elif num < 0:
        num = str(num)
        for _ in num:
            result += 1

        result -= 1

        print(result)

main()
