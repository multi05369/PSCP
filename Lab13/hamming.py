'''function'''
def hamming(text1, text2):
    '''solution'''
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance += 1

    print(distance)

hamming(str(input()), str(input()))
