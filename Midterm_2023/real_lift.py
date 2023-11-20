'''function'''
def lift():
    '''solution'''
    people = int(input())
    while people == 0:
        print("Safe")
        break
    heavy_mag = float(input())
    count_kilo = 0
    age = int(input())
    kilo = float(input())
    count_kilo += kilo
    for _ in range(people - 1):
        age_2 = int(input())
        kilo_2 = float(input())
        count_kilo += kilo_2
        if age < age_2:
            age = age_2
    if count_kilo > heavy_mag:
        print("Not Safe")
    elif age < 12:
        print("Not Safe")
    else:
         print("Safe")

lift()
