'''function'''
def diginity():
    '''solution'''
    while True:
        num = input()
        if num == "0":
            break
        check = 0
        for i in num:
            check += int(i)
            if check >= 10:
                check = int(str(check)[0]) + int(str(check)[1])
        print(check)

diginity()
