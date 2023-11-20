'''math for it'''
import math
def mathit(raduis):
    '''solution'''
    area = math.pi * (raduis**2)
    circumference = 2 * math.pi * raduis
    print("Area: %.3f" % area)
    print("Circumference: %.3f" % circumference)

mathit(float(input()))
