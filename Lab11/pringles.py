'''function'''
def pringles():
    '''solution'''
    box1 = input()
    contain = input()
    box2 = input()
    num_lenght = int(input())
    chrips = 0
    chripsin = 0
    eatchrips = contain[:num_lenght]
    noteat = contain[num_lenght:]
    for i in eatchrips:
        if i == ")":
            chrips += 1
    for j in noteat:
        if j == ")":
            chripsin += 1
    print(chrips)
    if chripsin == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(box1)
    print(" "*(num_lenght) + str(noteat))
    print(box2)
pringles()
