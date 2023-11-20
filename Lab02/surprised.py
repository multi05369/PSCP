'''function'''
def main():
    '''solution'''
    num_sum = float(input())
    highest = float(input())
    midscore = min(num_sum - highest, highest)
    lowerst = num_sum - highest - midscore
    if highest - lowerst > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
