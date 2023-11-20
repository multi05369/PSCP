'''function'''
def day_in_2011():
    '''solution'''
    day = int(input())
    month = int(input())

    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    if month < 3:
        month += 12
        year = 2010
    else:
        year = 2011
    kkk = year % 100
    jjj = year // 100

    day_of_week_index = (day + 13 * (month + 1) // 5 + kkk + kkk // 4 + jjj // 4 - 2 * jjj) % 7

    print(days_of_week[day_of_week_index])

day_in_2011()
