'''function'''
def kaprekars(num, count=0):
    '''solution'''
    while int(num) != 6174:
        if len(num) < 4:
            num += "0"
        highest = check_num(int(num[0]), int(num[1]), int(num[2]), int(num[3]), "high")
        lowest = check_num(int(num[0]), int(num[1]), int(num[2]), int(num[3]), "low")
        num = str(int(highest) - int(lowest))
        count += 1
    print(count)
def check_num(num1, num2, num3, num4, result):
    '''check num'''
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num1 > num4:
        num1, num4 = num4, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num2 > num4:
        num2, num4 = num4, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if result == "high":
        return "%d%d%d%d"% (num4, num3, num2, num1)
    elif result == "low":
        return "%d%d%d%d"% (num1, num2, num3, num4)

kaprekars(input())
