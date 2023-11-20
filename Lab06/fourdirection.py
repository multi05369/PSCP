'''function'''
def fourdirection():
    '''solution'''
    password = input()
    for i in range(len(password)):
        line1()
    print()
    for i in range(len(password)):
        line2(password, i)
    print()
    for i in range(len(password)):
        line3(password, i)
    print()
    for i in range(len(password)):
        line4(password, i)
    print()
    for i in range(len(password)):
        line1()
    print()
def line1():
    '''line1'''
    print("  *  ", end=" ")
def line2(password, roundnum):
    '''line2'''
    if password[roundnum] == "U":
        print(" *** ", end=" ")
    elif password[roundnum] == "D":
        print("  *  ", end=" ")
    elif password[roundnum] == "L":
        print(" *   ", end=" ")
    elif password[roundnum] == "R":
        print("   * ", end=" ")
def line3(password, roundnum):
    '''line3'''
    if password[roundnum] in "UD":
        print("* * *", end=" ")
    elif password[roundnum] in "LR":
        print("*****", end=" ")
def line4(password, roundnum):
    '''line4'''
    if password[roundnum] == "U":
        print("  *  ", end=" ")
    elif password[roundnum] == "D":
        print(" *** ", end=" ")
    elif password[roundnum] == "L":
        print(" *   ", end=" ")
    elif password[roundnum] == "R":
        print("   * ", end=" ")

fourdirection()
