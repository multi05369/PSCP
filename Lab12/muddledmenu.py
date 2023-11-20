'''function'''
def muddlemenu():
    '''solution'''
    menu = []
    while True:
        food = input()
        if food == "DONE":
            break
        elif food == "CLOSED":
            menu = []
            return print("Full Course: " + str(menu) +" Reversed: " + str(menu))
        elif food[0:10] == "Can't do: ":
            menu.remove(food[10:])
        elif food == "SOMETHING'S WRONG":
            menu = []
            continue
        else:
            food = food.split(" #")
            if food[1].isnumeric():
                menu.insert(int(food[1]) - 1, food[0])
            else:
                menu.append(food[0])
    print("Full Course: " + str(menu) + " Reversed: " + str(menu[::-1]))

muddlemenu()
