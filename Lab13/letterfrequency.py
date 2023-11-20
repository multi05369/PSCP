'''function'''
def letterfrequency(text):
    '''solution'''
    alphabetdict = dict()
    for i in text:
        if i.isalpha():
            alphabetdict[i] = alphabetdict.get(i, 0) + 1
    print(max(alphabetdict, key=alphabetdict.get))

letterfrequency(input().lower())
