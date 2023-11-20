'''function'''
def main():
    '''solution'''
    text = str(input())
    frame = len(text)
    print("*" * (frame + 2), end="")
    print()
    print("*" + text + "*")
    print("*" * (frame + 2), end="")

main()
