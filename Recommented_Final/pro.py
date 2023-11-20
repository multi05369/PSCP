'''function'''
def pro():
    '''solution'''
    come = int(input())
    paid = int(input())
    person_perbath = int(input())
    person = int(input())
    full = (person // come) * paid
    total = (full + (person % come)) * person_perbath
    print(total)

pro()
