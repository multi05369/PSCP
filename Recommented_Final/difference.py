'''function'''
import json
def difference():
    '''solution'''
    list1 = json.loads(input())
    list2 = json.loads(input())
    count1 = dict()
    count2 = dict()
    for i in list1:
        count1[i] = count1.get(i, 0) + 1
    for i in list2:
        count2[i] = count2.get(i, 0) + 1
    diff_dict = dict()
    for key in set(list1 + list2):
        diff = count1.get(key, 0) - count2.get(key, 0)
        if diff != 0:
            diff_dict[key] = diff
    for key in sorted(diff_dict):
        print(key, int(abs(diff_dict[key])))

    if not diff_dict:
        print("ONAJI DAYO!")

difference()
