'''function for blackjack game'''
def main():
    '''solution for calculate 21 game'''
    num_card = int(input(''))
    score_dict = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }
    score = 0
    num_aces = 0

    if num_card == 2:
        frist_card = input('')
        second_card = input('')
        score += score_dict[frist_card] + score_dict[second_card]
        if frist_card == 'A':
            num_aces += 1
        if second_card == 'A':
            num_aces += 1

    if num_card == 3:
        frist_card = input('')
        second_card = input('')
        third_card = input('')
        score += score_dict[frist_card] + score_dict[second_card] + score_dict[third_card]
        if frist_card == 'A':
            num_aces += 1
        if second_card == 'A':
            num_aces += 1
        if third_card == 'A':
            num_aces += 1

    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1

    print(score)

main()
