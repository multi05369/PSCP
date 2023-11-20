'''function'''
def main():
    '''solution'''
    var1 = abs(int(input()))
    var2 = abs(int(input()))
    var3 = abs(int(input()))

    num1 = int(str(var1) + str(var2) + str(var3))
    num2 = int(str(var1) + str(var3) + str(var2))
    num3 = int(str(var2) + str(var1) + str(var3))
    num4 = int(str(var2) + str(var3) + str(var1))
    num5 = int(str(var3) + str(var2) + str(var1))
    num6 = int(str(var3) + str(var1) + str(var2))

    mostnum = num1

    if num2 > mostnum:
        mostnum = num2
    if num3 > mostnum:
        mostnum = num3
    if num4 > mostnum:
        mostnum = num4
    if num5 > mostnum:
        mostnum = num5
    if num6 > mostnum:
        mostnum = num6

    print(mostnum)

main()
