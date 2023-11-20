'''function'''
def checkvalid(num):
    '''check valid'''
    for _ in range(num):
        text = input()
        if text.isidentifier() and (text != "if" and text != "else" and text != "elif" \
        and text != "while" and text != "for" and text != "True" and text != "False" and \
        text != "continue" and text != "break" and text != "return"\
        and text != "is" and text != "in" and text != "and"\
        and text != "or" and text != "from" and text != "as" and \
        text != "pass" and text != "not" and text != "def" and text != "None"):
            print("Valid")
        else:
            print("Invalid")

checkvalid(int(input()))
