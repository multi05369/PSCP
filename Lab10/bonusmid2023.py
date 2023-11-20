'''function'''
def bonus():
    '''solution'''
    salary = int(input())
    year = int(input())
    month = int(input())
    bonus_rate = 0
    if month >= 10:
        year += 1
    for _ in range(year):
        bonus_rate += 1
    if bonus_rate > 20:
        bonus_rate = 20
    bonus_total = salary * bonus_rate
    if bonus_total < 5000:
        bonus_total = 5000
    if bonus_total > 1000000:
        bonus_total = 1000000
    print(bonus_total)

bonus()
