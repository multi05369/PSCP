'''function'''
def missingcard():
    '''solution'''
    listcard = []
    listall = ['AS', 'KS', 'QS', 'JS', '10S',
               '9S', '8S', '7S', '6S', '5S',
               '4S', '3S', '2S', 'AH', 'KH', 'QH', 'JH', '10H',
               '9H', '8H', '7H', '6H', '5H',
               '4H', '3H', '2H', 'AD', 'KD', 'QD', 'JD', '10D',
               '9D', '8D', '7D', '6D', '5D',
               '4D', '3D', '2D', 'AC', 'KC', 'QC', 'JC', '10C',
               '9C', '8C', '7C', '6C', '5C',
               '4C', '3C', '2C',]
    count = 0
    while True:
        card = input()
        listcard.append(card)
        count += 1
        if count == 51:
            break
    for i in listall:
        if i not in listcard:
            print(i)

missingcard()
