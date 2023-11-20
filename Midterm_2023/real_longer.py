'''function'''
import math
def longer():
    '''solution'''
    raduis = abs(float(input()))
    height = abs(float(input()))
    lenght = abs(float(input()))

    res = (height + lenght) * 2
    res2 = 2 * math.pi * raduis
    if res2 > res:
        print("Circle is longer")
        res3 = res2 - res
        print("%.5f" % abs(res3))
    if res > res2:
        print("Rectangle is longer")
        res3 = res2 - res
        print("%.5f" % abs(res3))
    if res == res2:
        print("Equal")
        res3 = res2 - res
        print("%.5f" % abs(res3))

longer()
