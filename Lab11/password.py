'''function'''
import math
import string
def calculate_entropy(text):
    '''calculate entropy'''
    length = len(text)
    has_num = False
    has_small = False
    has_big = False
    has_punctuation = False
    for char in text:
        if char.isdecimal():
            has_num = True
        elif char.islower():
            has_small = True
        elif char.isupper():
            has_big = True
        elif char in string.punctuation:
            has_punctuation = True
    rrr = 0
    if has_num:
        rrr += 10
    if has_small:
        rrr += 26
    if has_big:
        rrr += 26
    if has_punctuation:
        rrr += 32
    entropy = math.log2(rrr ** length)
    return entropy
def password_strength(entropy):
    '''calculate strength'''
    if entropy >= 128:
        return "Very Strong"
    elif 60 <= entropy <= 127:
        return "Strong"
    elif 36 <= entropy <= 59:
        return "Reasonable"
    elif 28 <= entropy <= 35:
        return "Weak"
    else:
        return "Very Weak"
def password():
    '''solution'''
    text = input()
    entropy = calculate_entropy(text)
    entropy = int(entropy)
    print(entropy)
    strength = password_strength(entropy)
    print(strength)

password()
