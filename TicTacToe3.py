from TicTacToe2 import check_col,check_diag,check_line,check_endGame

def InputGame(game,actualPlayer,form):
    print()
    print(f"------------------------------------------------Actual Player:{actualPlayer}-----------------------------------------")
    print()

    row,col=0,0
    win=0
    print()
    alreadyChoose=False
    while ((row < 1 or col < 1 or row > 3 or col > 3) or (alreadyChoose==True)):
        alreadyChoose=False
        try:
            row,col=list(map(int, input("Where you want to move: (row,col) ").split(",")))
        except ValueError:
            continue
        try:
            if game[row-1][col-1]!=0:
                print()
                print("!!!!!!!!!!!!!!!!!!! CASE ALREADY TOOK !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                alreadyChoose=True
        except IndexError:
            pass
        
                
    row-=1
    col-=1
    game[row][col]=form
    if check_col(game) !=0 :
        win=check_col(game)
    elif check_line(game) !=0:
        win=check_line(game)
    elif check_diag(game) !=0:
        win=check_diag(game)
    elif check_endGame(game)== True:
        win=check_endGame(game)

    return win