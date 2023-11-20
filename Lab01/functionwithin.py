'''function'''
def function_f(aaa):
    '''calculate'''
    result1 = 2*aaa
    return result1

def function_g(aaa):
    '''calculate'''
    result2 = 3*(aaa**4) - (aaa**3) + 2*(aaa**2) + 10
    return result2

def function_h(aaa, bbb, ccc):
    '''calculate'''
    result3 = ((ccc + aaa)**2) - (aaa*bbb) + (bbb**2)
    return result3

def function_i(aaa, bbb, ccc, ddd):
    '''calculate'''
    result4 = (aaa**2 + bbb**2 - ccc**2) / (ddd**2 - 2*aaa*ddd + 2*aaa)
    return result4

def main():
    '''solution'''
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    fof = function_f(function_f(aaa))
    gof = function_g(function_f(aaa - bbb))
    hof = function_h(function_f(aaa + bbb), function_f(aaa + ccc), function_g(function_f(ddd**2)))
    iof = function_i(
        function_h(function_f(aaa + bbb), function_f(aaa - ccc), function_g(function_f(ddd ** 2))),
        function_g(function_f(aaa - bbb)),
        function_f(function_f(function_f(function_f(function_f(ccc))))),
        ddd ** 8)
    print(fof)
    print(gof)
    print(hof)
    print(iof)

main()
