'''function'''
def main():
    '''solution'''
    average = float(input())
    point1 = float(input())
    point2 = float(input())
    point3 = float(input())

    point4 = (average*4) - (point1 + point2 + point3)
    all_weight = point1 + point2 + point3 + point4

    if all_weight <= 15000:
        if (average / 2) <= (abs(average - point1)):
            print("Unbalance")
        elif (average / 2) <= (abs(average - point2)):
            print("Unbalance")
        elif (average / 2) <= (abs(average - point3)):
            print("Unbalance")
        elif (average / 2) <= (abs(average - point4)):
            print("Unbalance")
        else:
            print("Pass %.2f" % point4)
    else:
        print("Overweight")

main()
