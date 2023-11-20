'''function'''
def badkeyboard(text):
    '''solution'''
    res = ""
    for i in str(text):
        if i == "i":
            res += i.replace("i", "o")
        elif i == "o":
            res += i.replace("o", "i")
        elif i == "I":
            res += i.replace("I", "O")
        elif i == "O":
            res += i.replace("O", "I")
        else:
            res += i
    print(res)

badkeyboard(input())
