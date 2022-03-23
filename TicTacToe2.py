def check_line(game):
    winner="nobody"
    for line in game:
        print(line)
        if line[0]!=0 :
            if (line[0]==line[1]==line[2]):
                winner=line[0]
                return winner
    return 0

def check_col(game):
    for indice in range(3):
        ok=True
        number=game[0][indice]
        for col in game:
            if (col[indice]!=number or number==0):
                ok=False
        if ok:
            return number
    return 0

def check_diag(game):
    if game[1][1] !=0:
        if (game[0][0]==game[1][1]==game[2][2] or game[0][2]==game[1][1]==game[2][0]):
            return game[1][1]
    return 0


def check_endGame(game):
    # checking = False
    checking = True
    for line in game:
        for case in line:
            if case == 0:
                checking = False
                return False
            # checking = False if case == 0 else True
            # if not checking: break
        # if not checking: break
    return checking