'''function'''
import math
def longer():
    '''solution'''
    radius = float(input())
    height = float(input())
    lenght = float(input())

    res = 2 * math.pi * radius
    res2 = (height + lenght) * 2
    if res > res2:
        print("Circle is longer")
        print("%.5f" % abs(res - res2))
    elif res2 > res:
        print("Rectangle is longer")
        print("%.5f" % abs(res2 - res))
    elif res == res2:
        print("Equal")
        print("%.5f" %(res - res2))

longer()
