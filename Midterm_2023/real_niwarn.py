'''function'''
import math
def x_function(n):
    '''find x'''
    return 2 + ((math.log2(n**2)) / (2*n*(math.log2(n))))
def y_function(n, s):
    '''find y'''
    return (math.sin(math.radians(30)) + ((2*s)**0.5)) / (x_function(n) + 3)
def z_function(k):
    '''find z'''
    return y_2function(k) + ((8456 * x_4function(k)) / (24*k))
def y_2function(k):
    ''' find y**2'''
    return ((math.sin(math.radians(30)) + ((2*k)**0.5)) / (x_function(k) + 3))**2
def x_4function(k):
    '''find x**4'''
    return (x_function(k))**4
def niwarn():
    '''solution'''
    nnn = float(input())
    sss = float(input())
    kkk = float(input())
    x_point = x_function(nnn)
    y_point = y_function(nnn, sss)
    z_point = z_function(kkk)
    print("X: %.1f, Y: %.1f, Z: %.1f" % (x_point, y_point, z_point))

niwarn()
