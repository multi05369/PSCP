'''function'''
def converter():
    '''solution'''
    time = int(input())
    second_check = int(input())
    minute_check = int(input())
    hour_check = int(input())
    minute = time // second_check
    second = time % second_check
    hours = minute // minute_check
    minute = minute % minute_check
    hours = hours % hour_check
    print("%d:%d:%d" % (hours, minute, second))

converter()
