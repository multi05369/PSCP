'''function'''
def primenum(num):
    '''solution'''
    prime = True
    numpow = num**0.5
    numpow = int(numpow)
    if num > 1:
        for i in range(2, numpow + 1):
            if num % i == 0:
                prime = False
                break
    if prime and num != 1 and num != 0:
        print("Yes")
    else:
        print("No")

primenum(int(input()))
