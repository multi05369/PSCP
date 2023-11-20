'''function'''
def triangle_area(aaa, bbb, ccc):
    '''solution'''
    space = (aaa + bbb + ccc) / 2
    area = (space * (space - aaa) * (space - bbb) * (space - ccc))**0.5
    print("%.3f" % area)

triangle_area(float(input()), float(input()), float(input()))
