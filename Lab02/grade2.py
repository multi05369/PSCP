'''function'''
def main():
    '''solution'''
    score = float(input())

    if 95 <= score <= 100:
        print('A')
    elif 90 <= score < 95:
        print('B+')
    elif 85 <= score < 90:
        print('B')
    elif 80 <= score < 85:
        print('C+')
    elif 75 <= score < 80:
        print('C')
    elif 70 <= score < 75:
        print('D+')
    elif 65 <= score < 70:
        print('D')
    elif 60 <= score < 65:
        print('F+')
    elif 0 <= score < 60:
        print('F')
    elif score < 0 or score > 100:
        print('ERR')

main()
