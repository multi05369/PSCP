'''function'''
def coprime():
    '''solution'''
    num_a = int(input())
    num_b = int(input())
    while num_b:
        num_a, num_b = num_b, num_a % num_b
    if num_a == 1:
        print("YES")
        print(num_a)
    else:
        print("NO")
        print(num_a)

coprime()
