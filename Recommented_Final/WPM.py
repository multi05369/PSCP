'''function'''
def wpm(kid_or_ad, speed):
    '''solution'''
    if kid_or_ad == "Kids":
        print(kidcheck(speed))
    else:
        print(adultcheck(speed))

def kidcheck(speed):
    '''check wpm kids'''
    if speed < 11:
        return "Very Slow"
    elif 11 <= speed <= 20:
        return "Slow"
    elif 21 <= speed <= 30:
        return "Average"
    elif 31 <= speed <= 40:
        return "Fast"
    elif speed > 40:
        return "Very Fast"

def adultcheck(speed):
    '''check wpm adults'''
    if speed < 26:
        return "Very Slow"
    elif 26 <= speed <= 35:
        return "Slow/Beginner"
    elif 36 <= speed <= 45:
        return "Intermediate/Average"
    elif 46 <= speed <= 65:
        return "Fast/Advanced"
    elif 66 <= speed <= 80:
        return "Very Fast"
    elif speed > 80:
        return "Insane"

wpm(input(), int(input()))
