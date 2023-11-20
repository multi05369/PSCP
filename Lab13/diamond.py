'''function'''
def diamond():
    '''solution'''
    deep = int(input())
    lenght = int(input())
    gem = []
    cost_gem = []
    for _ in range(deep):
        floor = input().split()
        gem.append(floor)
    for i in range(lenght):
        cal = 0
        for j in gem:
            cal += int(j[i])
        cost_gem.append(cal)
    print(max(cost_gem))

diamond()
