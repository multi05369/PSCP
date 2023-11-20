'''function'''
def is_prime(num):
    '''check prime'''
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_prime(number):
    '''solution'''
    res = 0
    for i in range(2, number + 1):
        if is_prime(i):
            res += 1
    print(res)

all_prime(int(input()))
