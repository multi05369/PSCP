'''function'''
def main():
    '''solution'''
    christ = int(input())
    if (christ % 4 == 0 and christ % 100 != 0) or christ % 400 == 0:
        print("Yes")
    else:
        print("No")

main()
