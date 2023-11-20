'''function'''
def parellogram(text):
    '''solution'''
    length = len(text)
    for i in range(length):
        print(" " * (length - i - 1) + text[:i + 1])

    for i in range(1, length):
        print(text[i:] + " " * (length - i - 1))

parellogram(input())
