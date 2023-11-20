'''function'''
def main():
    '''solution'''
    idnumber = str(input())
    result = 0

    for i in idnumber:
        result += int(i)
        lastthree = idnumber[-3:]
        result2 = int(lastthree) * 10

    key = result + result2
    if int(key) < 1000:
        key += 1000
        print(str(key)[-4:])
    else:
        print(str(key)[-4:])

main()
