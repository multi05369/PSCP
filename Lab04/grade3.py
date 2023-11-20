'''function'''
def main():
    '''solution'''
    subject = int(input())
    total = 0
    for _ in range(subject):
        score = float(input())
        total += calgrade(score)
    average = total / subject
    print("%.2f" %((int((average)*100))/100))
def calgrade(score):
    '''calgrade'''
    result = 0
    if 95 <= score <= 100:
        result = 4
    elif 90 <= score < 95:
        result = 3.5
    elif 85 <= score < 90:
        result = 3
    elif 80 <= score < 85:
        result = 2.5
    elif 75 <= score < 80:
        result = 2
    elif 70 <= score < 75:
        result = 1.5
    elif 65 <= score < 70:
        result = 1
    elif 60 <= score < 65:
        result = 0.5
    elif 0 <= score < 60:
        result = 0
    return result

main()
