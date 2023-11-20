'''function'''
def parity():
    '''solution'''
    num = input()
    type_data = input()
    count = 0

    for i in num:
        if i == "1":
            count += 1

    if type_data == "Even":
        if count == 0 or count % 2 == 0:
            num = num + "0"
            print(num)
        else:
            num = num + "1"
            print(num)
    else:
        if count == 0 or count % 2 == 0:
            num = num + "1"
            print(num)
        else:
            num = num + "0"
            print(num)

parity()
