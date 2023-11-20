'''function'''
def biary(num):
    '''solution without built-in function'''
    res = ""
    if num == 0:
        res = "0"

    while num > 0:
        remainder = num % 2
        res = str(remainder) + res
        num = num // 2
    print(res)

biary(int(input()))
