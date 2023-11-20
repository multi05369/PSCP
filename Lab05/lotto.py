'''function'''
def checklotto():
    '''check lottory'''
    first_place = str(input())
    last_two = str(input())
    front_three = str(input())
    front_three2 = str(input())
    last_three = str(input())
    last_three2 = str(input())
    lotto_buy = str(input())
    price = 0

    if lotto_buy == first_place:
        price += 6000000
    if lotto_buy[4:] == last_two:
        price += 2000
    if lotto_buy[:3] == front_three:
        price += 4000
    if lotto_buy[:3] == front_three2:
        price += 4000
    if lotto_buy[3:] == last_three:
        price += 4000
    if lotto_buy[3:] == last_three2:
        price += 4000
    if int(lotto_buy) == (int(first_place) - 1) or int(lotto_buy) == (int(first_place) + 1) \
        and first_place != "000000" and first_place != "999999":
        price += 100000
    elif first_place == "000000" or first_place == "999999":
        if int(lotto_buy) == ((int(first_place) - 1) % 1000000) or int(lotto_buy) == \
             ((int(first_place) + 1) % 1000000):
            price += 100000
    print(price)

checklotto()
