'''function'''
def stile():
    '''solution'''
    count = 0
    state = False
    while True:
        action = str(input())
        if action == "C":
            state = True
        elif state == True and action == "P":
            count += 1
            state = False
        else:
            state = False

        if action == "END":
            break
    print(count)

stile()
