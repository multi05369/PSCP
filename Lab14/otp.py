'''function'''
def otp():
    '''solution'''
    while True:
        password = str(input())

        if password == '0':
            break
        check = [password.count(str(i)) for i in range(10)]
        if len(password) == 4 and check.count(2) == 1:
            print("Valid")
        elif len(password) == 6 and (check.count(2) == 2 or check.count(3) == 1):
            print("Valid")
        elif len(password) == 8 and (check.count(3) == 2 or check.count(2) == 3):
            print("Valid")
        else:
            print("Invalid")

otp()
