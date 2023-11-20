'''function'''
def pickagain():
    '''solution'''
    text = input().split(" ")
    count = 0
    mylist = []
    for i in text:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            mylist.append(i)
            count = 1
    for j in reversed(mylist):
        print(j)
    if count == 0:
        print("Nope")

pickagain()
