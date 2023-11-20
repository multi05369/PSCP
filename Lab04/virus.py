'''function'''
def main():
    '''solution'''
    text = str(input())
    check = "o"
    result = 0
    for virus in text:
        if virus == check:
            result += 1
    print(result)

main()
