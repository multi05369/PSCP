'''function'''
def calwin(player1, player2):
    '''for cal who win or draw'''
    if player1 == player2:
        return "DRAW"
    elif player1 == "R" and player2 == "S":
        return "A"
    elif player1 == "P" and player2 == "R":
        return "A"
    elif player1 == "S" and player2 == "P":
        return "A"
    else:
        return "B"

def calscore():
    '''cal score'''
    text = str(input())
    score_a = 0
    score_b = 0

    for i in range(0, len(text), 2):
        winner = calwin(text[i], text[i + 1])
        if winner == "A":
            score_a += 1
        elif winner == "B":
            score_b += 1

    if score_a > score_b:
        print("A win %d-%d" % (score_a, score_b))
    elif score_b > score_a:
        print("B win %d-%d" % (score_b, score_a))
    else:
        print("DRAW %d" % (score_a))

calscore()
