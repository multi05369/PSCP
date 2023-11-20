'''function'''
def seeker(text):
    '''solution'''
    res = 0
    save = ""
    for i in text:
        if i.isdigit():
            save += i
        elif save:
            res += int(save)
            save = ""
    if save:
        res += int(save)
    print(res)

seeker(input())
