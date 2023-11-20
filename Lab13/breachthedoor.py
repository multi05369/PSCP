'''function'''
import string
def breachthedoor():
    '''solution'''
    text = str(input()).split(" ")
    change = str.maketrans('', '', string.punctuation)
    for word in text:
        changed = word.translate(change)
        if len(changed) > 6 and changed.isalpha():
            print(changed, end=" ")

breachthedoor()
