'''function'''
def encode(text):
    '''how to encode'''
    res = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            res += str(count) + text[i - 1]
            count = 1

    res += str(count) + text[-1]
    print(res)

encode(input())
