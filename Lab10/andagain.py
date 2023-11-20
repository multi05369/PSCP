'''function'''
def andagain():
    '''solution'''
    text = input()
    text = text.replace(".", "")
    list1 = text.split(" ")
    vowel = set("AEIOUaeiou")
    list2 = []
    count = 0
    for i in list1:
        if len(i) >= 2 and sum(1 for char in i if char in vowel) >= 2:
            list2.append(i)
            count = 1
    for j in sorted(list2):
        print(j, sep="\n")
    if count == 0:
        print("Nope")

andagain()
