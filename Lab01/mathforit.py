'''fuction'''
import math
def main():
    '''solution'''
    pii = math.pi
    raduis = float(input())
    area = pii * (raduis**2)
    area2 = 2*pii*raduis
    print("Area: %.3f" %area)
    print("Circumference: %.3f" %area2)

main()
