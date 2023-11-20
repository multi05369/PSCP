'''function'''
def decode():
    '''how to decode'''
    text = input()
    res = ""
    for i in text:
        if i.isdigit():
            res += i
        else:
            print(i * int(res), end="")
            res = ""

decode()
