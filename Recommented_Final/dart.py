'''function'''
def dart(num):
    '''solution'''
    score = 0
    for _ in range(num):
        point = input().split()
        pointx = int(point[0])
        pointy = int(point[1])
        destination = (pointx**2 + pointy**2)**0.5
        if destination <= 2:
            score += 5
        elif destination <= 4:
            score += 4
        elif destination <= 6:
            score += 3
        elif destination <= 8:
            score += 2
        elif destination <= 10:
            score += 1
    print(score)

dart(int(input()))
