'''blackjack'''
def blackjack():
    '''solution'''
    card = int(input())
    count = 0
    num_ace = 0

    for _ in range(card):
        hand = input()
        if hand == "J":
            count += 10
        elif hand == "Q":
            count += 10
        elif hand == "K":
            count += 10
        elif hand == "A":
            count += 11
            num_ace += 1
        else:
            count += int(hand)

    while count > 21 and num_ace > 0:
        count -= 10
        num_ace -= 1

    print(count)

blackjack()
