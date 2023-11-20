'''function'''
def main():
    '''solution'''
    size = int(input())
    align = str(input())
    text = str(input())

    if align.lower() == "left":
        print(text.ljust(size))
    if align.lower() == "center":
        if (size - len(text)) % 2 == 0:
            print(text.center(size))
        else:
            print(text.center(size + 1))
    if align.lower() == "right":
        print(text.rjust(size))

main()
