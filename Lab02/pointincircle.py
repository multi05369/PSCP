'''function'''
def main():
    '''solution'''
    xxx = float(input())
    yyy = float(input())
    raduis = float(input())
    distance_x = float(input())
    distance_y = float(input())

    all_area2 = ((distance_x - xxx)**2 + (distance_y - yyy)**2)**0.5

    if all_area2 <= raduis:
        print("True")
    else:
        print("False")

main()
