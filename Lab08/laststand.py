'''function'''
import json
def laststand():
    '''solution'''
    text = str(input())
    for i in json.loads(text):
        print(str(i)[-1])

laststand()
