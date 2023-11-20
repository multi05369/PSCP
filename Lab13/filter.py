'''function'''
import json
def filterr():
    '''solution'''
    group_text = json.loads(input())
    criterion = float(input())
    filtered_score = []
    check = 0
    for i, j in group_text.items():
        if j >= criterion:
            filtered_score.append((i, j))
            check = 1
    if check == 0:
        print("Nope")
    else:
        filtered_score.sort(key=lambda x: x[0])
        for std in filtered_score:
            print("%s\t%.2f" % (std[0], std[1]))

filterr()
