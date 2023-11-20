'''function'''
def position(text):
    '''solution'''
    item_1 = 1
    item_2 = 0
    item_3 = 0

    for i in text:
        if i == "A":
            item_2, item_1 = item_1, item_2
        elif i == "B":
            item_3, item_2 = item_2, item_3
        elif i == "C":
            item_1, item_3 = item_3, item_1

    if item_1 == 1:
        print(1)
    elif item_2 == 1:
        print(2)
    else:
        print(3)

position(str(input()))
