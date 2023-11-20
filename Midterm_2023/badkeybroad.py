'''function'''
def badkeybroad():
    '''solution'''
    text = input()
    res = ""
    for i in text:
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

badkeybroad()
