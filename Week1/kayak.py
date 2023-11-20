'''function for calculate weigth boat'''
def main():
    '''solution how to calculate'''
    n_num = int(input())
    weigth = input().split(" ")
    for aaa in range(2*n_num):
        weigth[aaa] = int(weigth[aaa])
    weigth = sorted(weigth)
    check = 0
    answer = 0
    num_dif = 0

    while True:
        if len(weigth) > 2:
            for iii in range(len(weigth) - 1):
                if abs(weigth[iii] - weigth[iii+1]) == num_dif:
                    answer += num_dif
                    weigth.pop(iii)
                    weigth.pop(iii)
                    check = 1
                    break
        else:
            break

        if check == 1:
            check = 0
        else:
            num_dif += 1

    print(answer)

main()
