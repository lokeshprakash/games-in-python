 """            Start
                  │
                  ▼
          Import random module
                  │
                  ▼
      Create coordinate board (board1)
                  │
                  ▼
      Create empty game board (board)
                  │
                  ▼
         Ask game mode (1 or 2)
                  │
         ┌────────┴────────┐
         ▼                 ▼
   One Player         Two Players
         │                 │
         ▼                 ▼
 Display board layout  Display board layout
         │                 │
         ▼                 ▼
    Play up to 9 turns
         │
         ▼
 Place X or O using play()
         │
         ▼
 Display updated board
         │
         ▼
 Check winner using result()
         │
    ┌────┴────┐
    ▼         ▼
 Winner     No Winner
    │         │
    ▼         ▼
 End Game  Continue until 9 turns """
import random
board1 = [
    ['0 0 ', '0 1 ', '0 2 '],
    ['1 0 ', '1 1 ', '1 3 '],
    ['2 0 ', '2 1 ', '2 2 ']


]
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']


]
def bord():
    for i in board:
        print('|'.join(i))
def play(n,m,i):
    if board[n][m]==' ':
        if i%2!=0:
            board[n][m] = 'x'
        else:
            board[n][m]='o'
    else:
        print("already occupied")
def result():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            print(board[i][0], "wins")
            return True

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            print(board[0][j], "wins")
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        print(board[0][0], "wins")
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        print(board[0][2], "wins")
        return True

    return False
n=0
m=0
def twovs():
    for i in range(1,10):
        if i%2==0:
            print("player 2")
            n=int(input())
            m=int(input())
            play(n,m,i)
            bord()
            if result():
                print("player2")
                break
            else:
                print("continue")
        
        else:
            print("player 1")
            n=int(input())
            m=int(input())
            play(n,m,i)
            bord()
            if result():
                print("player1")
                break
        
            else:
                print("continue")
def onevs():
    for i in range(1,10):
        if i%2==0:
            print("player 2")
            n=int(input())
            m=int(input())
            play(n,m,i)
            bord()
            if result():
                print("player2")
                break
            else:
                print("continue")
        
        else:
            print("player 1")
            n=random.randint(0,2)
            m=random.randint(0,2)
            play(n,m,i)
            bord()
            if result():
                print("player1")
                break
        
            else:
                print("continue")
w=int(input("if 2 player input 2 if one player in put 1"))
if w==1:
    
    print("layout")
    for i in board1:
        print('|'.join(i))
    onevs()
    
else:
    
    print("layout")
    for i in board1:
        print('|'.join(i))
    twovs()
    
    
