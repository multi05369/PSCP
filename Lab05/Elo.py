'''Elo'''
def elo(raa, rbb, team):
    '''solution'''
    if team == "A":
        team_a = 1 / (1 + (10**((rbb - raa) / 400)))
        print("%.2f" % team_a)
    elif team == "B":
        team_b = 1 / (1 + (10**((raa - rbb) / 400)))
        print("%.2f" % team_b)

elo(int(input()), int(input()), str(input()))
