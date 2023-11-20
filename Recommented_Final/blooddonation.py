'''function'''
def blood():
    '''solution'''
    age = int(input())
    weight = int(input())
    donated = int(input())
    agecheck = False
    weightcheck = False
    permissioncheck = True
    candonated = False
    if age == 17 or 60 <= age <= 70:
        permissioncheck = False
        permission = str(input()) #True or False
        if permission == "True":
            permissioncheck = True
    if 17 <= age <= 70:
        agecheck = True
    if weight >= 45:
        weightcheck = True
    if donated == 0 and age < 55:
        candonated = True
    if donated > 0:
        candonated = True
    if agecheck and weightcheck and candonated and permissioncheck:
        print("Yes")
    else:
        print("No")

blood()
