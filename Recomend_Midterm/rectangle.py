'''function'''
def area_rec(height, lenght):
    '''area of rectangle'''
    area = height * lenght
    return area

def circum_rec(height, lenght):
    '''circumference of rectangle'''
    circum = (height + lenght) * 2
    return circum

def rectangle(height, lenght):
    '''solution'''
    area = area_rec(height, lenght)
    circumference = circum_rec(height, lenght)
    print(area)
    print(circumference)

rectangle(int(input()), int(input()))
