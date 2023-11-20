'''function'''
def bigframe():
    '''solution'''
    text = input().rstrip()
    text2 = input().rstrip()
    text3 = input().rstrip()
    text4 = input().rstrip()
    text5 = input().rstrip()
    longest = text
    texts = [text, text2, text3, text4, text5]
    for word in texts:
        if len(word) > len(longest):
            longest = word
    frame = len(longest) + 4
    print("*" * frame)
    print("* " + text + " "* (len(longest) - len(text)) + " *")
    print("* " + text2 +" "* (len(longest) - len(text2)) + " *")
    print("* " + text3 +" "* (len(longest) - len(text3)) + " *")
    print("* " + text4 +" "* (len(longest) - len(text4)) + " *")
    print("* " + text5 +" "* (len(longest) - len(text5)) + " *")
    print("*" * frame)

bigframe()
