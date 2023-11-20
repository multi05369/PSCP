'''function'''
def main():
    '''solution'''
    text = str(input())
    if text.isdecimal() == True:
        print("Number")
    elif text.isupper() == True:
        print("Uppercase")
    elif text.islower() == True:
        print("Lowercase")
    elif text.istitle() == True:
        print("Title")
    elif text.isspace() == True:
        print("Space")
    else:
        print("Other")

main()
