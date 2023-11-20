'''function'''
def helloooo():
    '''solution'''
    vowels = "aeiou"
    text = input()
    last_vowel_position = -1
    for i in range(len(text) - 1, -1, -1):
        if text[i] in vowels:
            last_vowel_position = i
            break
    if last_vowel_position != -1:
        last_vowel = text[last_vowel_position]
        behind = text[last_vowel_position + 1:]
        res = text[:last_vowel_position] + last_vowel * 4 + behind
    else:
        res = text
    print(res)

helloooo()
