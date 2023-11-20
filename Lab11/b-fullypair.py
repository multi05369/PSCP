'''function'''
def fullypair():
    '''solution'''
    text = input().lower()
    box = ""
    notpair = ""
    count = 0
    for char in text:
        if box.count(char) <= 0:
            box += char
    for char in box:
        if text.count(char) % 2 != 0:
            notpair += char
            count = 1
    if count == 0:
        print("fully paired")
    else:
        print(notpair)

fullypair()
