'''function'''
def catparade():
    '''solution'''
    catlist = []
    species = []
    while True:
        line = input()
        if line == "END":
            break
        elif line != "IT'S A DOG":
            for cat in line.split(","):
                catlist.append(cat.strip())
                if species.count(cat.strip()) == 0:
                    species.append(cat.strip())
        elif line == "IT'S A DOG":
            catlist.pop()
            species.pop()
    species.sort()
    for i in species:
        print(i, catlist.index(i) + 1, catlist.count(i))

catparade()
