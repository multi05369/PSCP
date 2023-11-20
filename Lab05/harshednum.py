'''function'''
def harshed():
    '''solution'''
    rob = 0
    while True:
        count = 0
        num = abs(int(input()))
        for j in str(num):
            count += int((j))
        if num == 0:
            print("No")
        elif num % count == 0:
            print("Yes")
        else:
            print("No")
        rob += 1
        if rob == 10:
            break

harshed()
