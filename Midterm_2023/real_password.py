'''function'''
import math
def password(text):
    '''solution'''
    lll = len(text)
    if text.islower():
        rrr = 26
    elif text.isalpha():
        rrr = 52
    elif text.isalnum():
        rrr = 62
    elif text.isprintable():
        rrr = 94
    entropy = math.log2(rrr**lll)
    entropy = math.floor(entropy)
    if entropy >= 128:
        strong = "Very Strong"
    elif 60 < entropy < 127:
        strong = "Strong"
    elif 36 < entropy < 59:
        strong = "Reasonable"
    elif 28 < entropy < 35:
        strong = "Weak"
    else:
        strong = "Very Weak"
    print(entropy)
    print(strong)

password(input())
