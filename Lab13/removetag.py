'''function'''
def removetag(text):
    '''solution'''
    word = list(filter(lambda x, check="<": check not in x, text))
    res = " ".join(word)
    print(res.split())

removetag(input().replace("<", "$<").replace(">", ">$").split("$"))
