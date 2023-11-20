'''function'''
def main():
    '''solution'''
    weightstart = int(input())
    weightend = int(input())
    text = "pass : "
    result = 0
    if weightstart < weightend:
        for item in range(weightstart, weightend + 1):
            if item % 2 == 0:
                text += str(abs(item)) + " "
                result += item
    else:
        for item in range(weightstart, weightend - 1, -1):
            if item % 2 == 0:
                text += str(abs(item)) + " "
                result += item

    print(text)
    print("Sum : %d" % abs(result))

main()
