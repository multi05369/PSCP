'''function'''
def centuries(num):
    '''solution'''
    for _ in range(num):
        year = input()

        if "B.E." in year:
            year = int(year.replace("B.E.", "")) - 543
            century = (year + 99) // 100
        elif "A.D." in year:
            year = int(year.replace("A.D.", ""))
            century = (year + 99) // 100
        else:
            century = "ERROR"
        print(century)

centuries(int(input()))
