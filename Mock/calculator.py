'''function'''
def calculator(num):
    '''solution'''
    res = ""
    for i in range(1, num + 1):
        if i == num:
            res += str(i) + "="
        else:
            res += str(i) + "+"

    if num == 1:
        res = "1"
        print(len(res))
    else:
        print(len(res))
calculator(int(input()))
