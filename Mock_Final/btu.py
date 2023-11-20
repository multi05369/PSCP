'''function'''
def btu551_2500(room):
    '''check btu'''
    global ratebtu
    if 551 <= room <= 700:
        ratebtu = 14000
    elif 701 <= room <= 1000:
        ratebtu = 18000
    elif 1001 <= room <= 1200:
        ratebtu = 21000
    elif 1201 <= room <= 1400:
        ratebtu = 23000
    elif 1401 <= room <= 1500:
        ratebtu = 24000
    elif 1501 <= room <= 2000:
        ratebtu = 30000
    elif 2001 <= room <= 2500:
        ratebtu = 34000

def calbtu(ratebtu, people, type_room, pos, addbtu):
    '''cal btu'''
    add_byper = 0
    add_bytype = 0
    change = 0
    all_rate = 0
    if people > 2:
        add_byper = abs(people - 2) * 600
    if type_room == "kitchen":
        add_bytype = 4000
    all_rate = ratebtu + add_byper + add_bytype + addbtu
    if pos == "facing the sun":
        change = (10 / 100) * all_rate
        all_rate = all_rate + change
    if pos == "shaded":
        change = (10 / 100) * all_rate
        all_rate = all_rate - change
    return int(all_rate)

def btu100_550():
    '''solution'''
    room = int(input())
    height = int(input())
    people = int(input())
    type_room = input() #kitchen or normol
    pos = input() #facing the sun or shaded or normol
    add_btu = 0
    global ratebtu

    if height > 8:
        diff = abs(8 - height)
        add_btu = 1000 * diff

    if 100 <= room <= 150:
        ratebtu = 5000
    elif 151 <= room <= 250:
        ratebtu = 6000
    elif 251 <= room <= 300:
        ratebtu = 7000
    elif 301 <= room <= 350:
        ratebtu = 8000
    elif 351 <= room <= 400:
        ratebtu = 9000
    elif 401 <= room <= 450:
        ratebtu = 10000
    elif 451 <= room <= 550:
        ratebtu = 12000
    elif room >= 551:
        btu551_2500(room)
    print(calbtu(ratebtu, people, type_room, pos, add_btu))

btu100_550()
