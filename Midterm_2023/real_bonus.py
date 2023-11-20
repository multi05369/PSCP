'''function'''
def bonus():
    '''solution'''
    salary = int(input())
    year = int(input())
    month = int(input())
    if salary < 5000:
        salary = 5000
        year = 1
        if month >= 10:
            year = 1
    if month >= 10:
        year += 1
    elif 0 <= month < 10:
        year += 0
    if salary * year > 1000000:
        year = 20
    if year == 0:
        year = 1
    res = (salary * year)
    if res > 1000000:
        res = 1000000
    print(res)

bonus()
