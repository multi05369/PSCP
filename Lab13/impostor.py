'''function'''
import json
def impostor():
    '''solution'''
    ingame = dict()
    alive = {}
    die = {}
    impo = 0
    while True:
        player = (input())
        if player.lower() == "end":
            break
        if player.lower() == "start":
            continue
        if player[0] == "{":
            ingame.update(json.loads(player))
        else:
            die.update({player: ingame[player]})
    for i in ingame:
        if i not in die:
            alive.update({i: ingame[i]})
    for j in alive:
        if alive[j] == "Impostor":
            impo += 1
    print("%d Impostor Remains" % impo)
    print("***Alive***")
    for k in sorted(alive):
        print("%s : %s" % (k, alive[k]))
    print("***Dead***")
    for i in sorted(die):
        print("%s : %s" % (i, die[i]))

impostor()
