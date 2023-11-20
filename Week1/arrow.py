'''function for create arrow'''
def main():
    '''solution for create arrow'''
    length = int(input(''))
    odd_number = int(input(''))

    for iii in range(odd_number):
        if iii < (odd_number // 2):
            spaces = (odd_number // 2) - iii
        else:
            spaces = iii - (odd_number // 2)
        print(" " * spaces + "*" * length)

main()
