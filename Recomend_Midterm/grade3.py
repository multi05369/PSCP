'''function'''
def check_grade(score):
    '''cal grade'''
    if 95 <= score <= 100:
        score = 4
    elif 90 <= score < 95:
        score = 3.5
    elif 85 <= score < 90:
        score = 3
    elif 80 <= score < 85:
        score = 2.5
    elif 75 <= score < 80:
        score = 2
    elif 70 <= score < 75:
        score = 1.5
    elif 65 <= score < 70:
        score = 1
    elif 60 <= score < 65:
        score = 0.5
    elif 0 <= score < 60:
        score = 0
    return score

def grade():
    '''solution'''
    num = int(input())
    sum_score = 0
    for _ in range(num):
        score = (float(input()))
        sum_score += check_grade(score)
    final_grade = sum_score / num
    print("%.2f" %((int((final_grade)*100))/100))

grade()
