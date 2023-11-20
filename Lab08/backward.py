'''function'''
def backward():
    '''solution'''
    mylist = []
    while True:
        text = str(input())
        if text == "NULL":
            break
        mylist.append(text)
    for i in reversed(mylist):
        print(i)

backward()
