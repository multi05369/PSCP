'''function'''
def linesort():
    '''solution'''
    num = int(input())
    mylist = []
    for _ in range(num):
        text = str(input())
        mylist.append(text)
    mylist.sort(key=checklen)
    for i in mylist:
        print(i)

def checklen(txt):
    '''checklen'''
    return len(txt)

linesort()
