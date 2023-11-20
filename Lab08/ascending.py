'''function'''
def ascending():
    '''solution'''
    mylist = []
    for _ in range(5):
        num = int(input())
        mylist.append(num)
    for i in sorted(mylist):
        print(i)

ascending()
