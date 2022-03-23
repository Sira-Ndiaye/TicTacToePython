from TicTacToe1 import gameDraw
from TicTacToe2 import check_col,check_diag,check_line
from TicTacToe3 import InputGame

# Game Initialisation
game=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


# Playes
player1=input("Player One: ").upper()
player2=input("Player Two: ").upper()
actualPlayer=player1
print("""
    ------------------------------------------------RULES-----------------------------------------
    -YOU ALWAYS INPUT TWO NUMBERS IN THE FORMAT (ROW,COL): DEPENDING WHERE YOU WANNA PLAY
     
    -YOU HAVE 3 ROWS AND 3 COLUMUMS 
    
    -!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  INDEX ARE BETWEEN 1 AND 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    -THE FIRST CASE LOCALISATION IS 1,1
    
    -READ AGAIN THE RULES
    ----------------------------------------------------------------------------------------------
                                                STARTING
                                            
""")
win=0

while(win==0 or win ==False):
    gameDraw(game)
    form="X" if actualPlayer==player1 else "V"
    win=InputGame(game,actualPlayer,form)
    actualPlayer=player2 if actualPlayer==player1 else player1
else:
    if win == True:
        print("END GAME ------- NO ONE WINS")
    else:
        gameDraw(game)
        winner=player1 if win=="X" else player2
        print()
        print(f"{winner} WON")
    


