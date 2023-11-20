'''function'''
def almostmean(num):
    '''solution'''
    stdlist = []
    total = 0
    for _ in range(num):
        student = input().split("\t")
        stdlist.append(student)
    for score in stdlist:
        total += float(score[1])
    mean = total / num

    closest_student = None
    closest_difference = float('inf')
    for student in stdlist:
        score = float(student[1])
        difference = abs(score - mean)
        if score <= mean:
            if difference < closest_difference:
                closest_difference = difference
                closest_student = student
    print("%s\t%s" %(closest_student[0], closest_student[1]))

almostmean(int(input()))
