'''function'''
def main():
    '''solution'''
    option = str(input())
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    check_ascend(option, num1, num2, num3)
    check_descend(option, num1, num2, num3)

def check_ascend(option, num1, num2, num3):
    '''checkAscend'''
    if option == "Ascend":
        if num1 <= num2 <= num3:
            print("%.2f, %.2f, %.2f" % (num1, num2, num3))
        elif num1 <= num3 <= num2:
            print("%.2f, %.2f, %.2f" % (num1, num3, num2))
        elif num2 <= num1 <= num3:
            print("%.2f, %.2f, %.2f" % (num2, num1, num3))
        elif num2 <= num3 <= num1:
            print("%.2f, %.2f, %.2f" % (num2, num3, num1))
        elif num3 <= num1 <= num2:
            print("%.2f, %.2f, %.2f" % (num3, num1, num2))
        elif num3 <= num2 <= num1:
            print("%.2f, %.2f, %.2f" % (num3, num2, num1))

def check_descend(option, num1, num2, num3):
    '''checkDescend'''
    if option == "Descend":
        if num1 >= num2 >= num3:
            print("%.2f, %.2f, %.2f" % (num1, num2, num3))
        elif num1 >= num3 >= num2:
            print("%.2f, %.2f, %.2f" % (num1, num3, num2))
        elif num2 >= num1 >= num3:
            print("%.2f, %.2f, %.2f" % (num2, num1, num3))
        elif num2 >= num3 >= num1:
            print("%.2f, %.2f, %.2f" % (num2, num3, num1))
        elif num3 >= num1 >= num2:
            print("%.2f, %.2f, %.2f" % (num3, num1, num2))
        elif num3 >= num2 >= num1:
            print("%.2f, %.2f, %.2f" % (num3, num2, num1))

main()
