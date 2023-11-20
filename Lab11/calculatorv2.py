'''function'''
def calculator(num):
    '''solution'''
    if num == 1:
        return 1
    num_str = str(num)
    num_digits = len(num_str)
    total_presses = 0
    for i in range(1, num_digits):
        total_presses += i * (9 * (10 ** (i - 1)))
    total_presses += num_digits * (num - 10 ** (num_digits - 1) + 1)
    return total_presses

print(calculator(int(input())))
