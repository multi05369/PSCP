'''function'''
def histogram(text):
    '''solution'''
    alphabet = dict()
    for i in text:
        if not i.isspace():
            alphabet[i] = alphabet.get(i, 0) + 1
    for j in sorted(alphabet.keys(), \
        key=lambda x: ord(x) + ((32.1 if x.isupper() else 0))):
        print(j, "=", alphabet[j])

histogram(input())
