'''function'''
def fibonacci_v2_helper(num, current=0, next_num=1, counter=0):
    '''use for help'''
    if counter == num:
        return current
    else:
        return fibonacci_v2_helper(num, next_num, current + next_num, counter + 1)

def fibonacci_v2(num):
    '''solution'''
    if num < 2:
        return num

    return fibonacci_v2_helper(num, 0, 1, 2)

print(fibonacci_v2(num=int(input())))
