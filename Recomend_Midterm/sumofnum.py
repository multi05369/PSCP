'''function'''
def sumofnum():
    '''solution'''
    num_set = int(input())
    count = 0
    while True:
        num = int(input())
        if num == -1:
            break
        count += num
        if count == num_set:
            break
    print(count)

sumofnum()
