'''function'''
import json
def pickthem():
    '''solution'''
    text = input()
    count = 0
    for i in json.loads(text):
        if i % 2 == 0:
            print(i)
            count = 1
    if count == 0:
        print("Nope")

pickthem()
