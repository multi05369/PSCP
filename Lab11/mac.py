'''function'''
def mac():
    '''solution'''
    text = input()
    char = "ABCDEFabcdef0123456789.:-"
    if len(text) != 17 and len(text) != 14:
        return print("ERROR")

    if not all(c in char for c in text):
        return print("ERROR")

    if not (text.count(":") == 5 or text.count(".") == 2 or \
        text.count("-") == 5):
        return print("ERROR")

    if text[2] == '-' and text[5] == '-' and text[8] == '-' \
        and text[11] == '-' and text[14] == '-':
        print("VALID 1")
    elif text[2] == ':' and text[5] == ':' and text[8] == ':' \
        and text[11] == ':' and text[14] == ':':
        print("VALID 2")
    elif text[4] == '.' and text[9] == '.' and text[:4].isalnum() \
        and text[5:9].isalnum() and text[10:].isalnum():
        print("VALID 3")
    else:
        print("ERROR")

mac()
