import pyfiglet
result=pyfiglet.figlet_format('Tic Tac Toa',font='3x5')
print(result)
game_board=[['- ','- ','- '],['- ','- ','- '],['- ','- ','- ']]
score=[[4,4,4],[4,4,4],[4,4,4]]

def show():
    for row in game_board:
        for cell in row:
          print(cell,end='')
        print()

def check_game():
    sum=8*[0]
    k=2
    t=0
    for i in range(3):
        for j in range(3):
            sum[t]=score[i][j]+sum[t]
            sum[t+1]=score[j][i]+sum[t+1]
        t+=2
        sum[-2]=score[i][i]+sum[-2]
        sum[-1]=score[i][k]+sum[-1]
        k-=1
        
    if 3 in sum:
        return 1
    if -3 in sum:
        return 2
    for x in sum :
        if x>3:
            return 3
    return 0

def show_result(x):
    if x==1:
        print('\nplayer1 win')
        show()
        time.sleep(3)
        exit(0)
    elif x==2:
        print('\nplayer2 win')
        show()
        time.sleep(3)
        exit(0)
    elif x==0:
        print('\nequal')
        show()
        time.sleep(3)
        exit(0) 

import time
show()
while True:
    while True:
        print('\nplayer 1')
        row=int(input('Row: '))
        col=int(input('column: '))
        if 1<=row<=3 and 1<=col<=3 :
            if game_board[row-1][col-1]=='- ':
                game_board[row-1][col-1]='X '
                score[row-1][col-1]=1
                b=check_game()
                show_result(b)
                break
            else:
                print('Input coordinates are duplicated')
        else :
            print('out of range!')
     
         
    show()
    while True:
        print('\nplayer 2')
        row=int(input('Row: '))
        col=int(input('Col: '))
        if 1<=row<=3 and 1<=col<=3:
            if game_board[row-1][col-1]=='- ':
                game_board[row-1][col-1]='O '
                score[row-1][col-1]=-1
                b=check_game()
                show_result(b)
                break
            else:
                print('Input coordinates are duplicated')
        else:
             print('out of range!')
       
    show()





 
