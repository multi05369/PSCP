'''function'''
def function_f(number):
    '''solution'''
    result = 2 * number
    return result

def function_g(number):
    '''solution'''
    result = (number / 2) + 1
    return result

def main():
    '''result'''
    number = int(input())
    number = number
    fog = function_f(function_g(number))
    gof = function_g(function_f(number))
    print("%.2f" %fog)
    print("%.2f" %gof)

main()
