'''function'''
def main():
    '''solution'''
    xxx = float(input())
    yyy = float(input())
    raduis_me = float(input())
    xxx_friend = float(input())
    yyy_friend = float(input())
    raduis_friend = float(input())

    dist = ((xxx_friend - xxx)**2 + (yyy_friend - yyy)**2)**0.5
    total_radius = raduis_friend + raduis_me

    if dist < total_radius:
        print("Yes")
    else:
        print("No")

main()
