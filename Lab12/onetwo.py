'''function'''
def onetwo_recursive(num):
    '''solution'''
    if num == 1:
        return "1"
    elif num == 2:
        return "2"
    else:
        return onetwo_recursive(num - 1) + onetwo_recursive(num - 2)

print(onetwo_recursive(int(input())))
