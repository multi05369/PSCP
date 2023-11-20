'''function'''
def word(text):
    '''solution'''
    for i in range(1, len(text) + 1):
        print(text[:i])

word(input())
