'''nearer'''
def nearer(alice, bob, ice):
    '''solution'''
    if abs(ice - alice) < abs(ice - bob):
        print("Alice %d" % abs(ice - alice))
    elif abs(ice - bob) < abs(ice - alice):
        print("Bob %d" % abs(ice - bob))
    else:
        print("Sundaes %d" % abs(ice - alice))

nearer(int(input()), int(input()), int(input()))
