'''function'''
def find_gcd():
    '''solution'''
    num_a = int(input())
    num_b = int(input())
    while num_b:
        num_a, num_b = num_b, num_a % num_b

    print(num_a)

find_gcd()
