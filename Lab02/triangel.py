'''function'''
def main():
    '''solution'''
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2

    if abs(num3**2 - (num1**2 + num2**2)) <= 0.01:
        print("Yes")
    else:
        print("No")

main()
