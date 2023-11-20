'''function'''
def palindrome():
    '''solution'''
    num = int(input())
    time = input()
    count = 0
    while count != num:
        second = "%02d" % (int(time[-2:]) + 1)
        hour = time[0:2].replace(":", "")
        if int(second) % 60 == 0 and int(second) != 0:
            second = "00"
            check_val = int(hour) + 1
            hour = str(check_val)
        if int(hour) % 24 == 0:
            hour = "0"
        time = hour + ":" + second
        if time.replace(":", "") == time[::-1].replace(":", ""):
            count += 1
            print(time)

palindrome()
