'''function'''
def histogram(text):
    '''solution'''
    alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    char_count = []

    for char in alphabet:
        count = text.count(char)
        if count > 0:
            char_count.append([char, count])
    sorted_chars = sorted(char_count, key=lambda x: x[0].lower())

    for char, count in sorted_chars:
        print(char + " = " + str(count))

histogram(input())
