'''function'''
def tuckofwar():
    '''solution 10 vs 10'''
    power_a = 0
    power_b = 0

    for _ in range(10):
        player = int(input())
        power_a += player
    for _ in range(10):
        player2 = int(input())
        power_b += player2

    if power_a > power_b:
        print("B")
    elif power_b > power_a:
        print("A")
    else:
        print("AB")

tuckofwar()
