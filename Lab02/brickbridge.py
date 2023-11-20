'''function'''
def main():
    '''solution'''
    ita_brick = int(input())
    itb_brick = int(input())
    goal = int(input())

    if itb_brick * 5 + ita_brick >= goal and goal % 5 <= ita_brick:
        if itb_brick * 5 < goal:
            result = goal - itb_brick * 5
        else:
            result = goal - ((goal // 5) * 5)
        print(result)
    else:
        print(-1)

main()
