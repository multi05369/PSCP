"""function"""
def main(amount):
    """solution"""
    result = dict()
    for _ in range(amount):
        song = input().split('-')
        if song[0] not in result.keys():
            result[song[0]] = [song[1]]
        else:
            result[song[0]].append(song[1])
    for k, vvv in result.items():
        print(k)
        print('\n'.join(map(str, vvv)))

main(int(input()))
