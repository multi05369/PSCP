'''function'''
def virus(text):
    '''solution'''
    coun = ""
    text = text.replace("O", "")
    for i in text:
        coun += (i)
    print(len(coun))
virus(input())
help(str)