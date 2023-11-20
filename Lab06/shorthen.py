'''function'''
def short():
    '''solution'''
    shortened = ""
    start = -1
    end = -1

    while True:
        num = int(input(""))
        if num == -1:
            break

        if num == end + 1:
            end = num
        else:
            if start == -1:
                shortened += str(end) + ", "
            elif start == end:
                shortened += str(start) + ", "
            else:
                shortened += str(start) + "-" + str(end) + ", "
        start = end = num

    if start == -1:
        shortened = shortened.rstrip(", ")
    elif start == end:
        shortened += str(start) + ", "
    else:
        shortened += str(start) + "-" + str(end) + ", "

    print(shortened.rstrip(", "))

short()
