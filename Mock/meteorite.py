'''function'''
def meteorite(kilo, bbb, safe):
    '''solution'''
    split = kilo / bbb
    count = 0
    while True:
        count += 1
        if split < safe:
            break
        else:
            split = split / 2
    print(count)

meteorite(float(input()), int(input()), float(input()))
