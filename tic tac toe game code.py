def printboard(board):
    for i in range(1,4):
        if i==2:
            print(" {} | {} | {} ".format(board[1],board[2],board[3]))
        else:
            print("   |   |   ")
    print("--------------")
    for i in range(1,4):
        if i==2:
            print(" {} | {} | {} ".format(board[4],board[5],board[6]))
        else:
            print("   |   |   ")
    print("--------------")
    for i in range(1,4):
        if i==2:
            print(" {} | {} | {} ".format(board[7],board[8],board[9]))
        else:
            print("   |   |   ")
def swapcurrplayer(currplayer):
    if currplayer==1:
        return 2
    else:
        return 1
def inputboard(playerssetup,currplayer,inpposn,board):
    board[inpposn]=playerssetup[currplayer]
    return board
def board_status(board):
    for i in range(1,10):
        if board[i]==" ":
            return True
    return False
    #this func can be also : return " " in board
def checkcurrplayerwonornot(playerssetup,currplayer,inpposn,board):
    rowno=((inpposn-1)/3)
    if board[3*rowno+1]==playerssetup[currplayer] and board[3*rowno+2]==playerssetup[currplayer] and board[3*rowno+3]==playerssetup[currplayer]:
        return True
    colno=(inpposn-1)%3
    if board[colno+1]==playerssetup[currplayer] and board[colno+4]==playerssetup[currplayer] and board[colno+7]==playerssetup[currplayer]:
        return True
    #if inpposn==5 and ((board[1]==playerssetup[currplayer] and board[9]==playerssetup[currplayer]) or (board[3]==playerssetup[currplayer] and board[7]==playerssetup[currplayer])):
    #    return True
    if rowno!=1 and colno!=1 and board[5]==playerssetup[currplayer] and board[inpposn]==playerssetup[currplayer] and board[10-inpposn]==playerssetup[currplayer]:
        return True
    return False
def playtictactoe():
    playerssetup1=("","X","O")
    playerssetup2=("","O","X") #TUPLES IMPROVE DATA SECURITY SO SHOULD USE TUPLES AS MOST AS WE CAN
    board=[""," "," "," "," "," "," "," "," "," "]
    print("WELCOME TO TIC TAC TOE GAME:")
    inp=input("PLAYER 1 : DO YOU WANT TO BE X OR O ?")
    print("Player 1 will go first:")
    if inp=='X':
        playerssetup=playerssetup1
    else:
        playerssetup=playerssetup2
    printboard(board)
    currplayer=1
    while board_status(board):#TIE CAN HAPPEN ONLY WHEN ALL POSITIONS ON BOARD ARE OCCUPIED..
        inpposn=int(input("Player {} enter Position B/W (1-9) where you want to mark {}".format(currplayer,playerssetup[currplayer])))
        #ASSUMING PLAYER WILL ALWAYS INPUT A PLACE WHICH IS NOT OCCUPIED TILL NOW AND B/W 1 ND 9
        board=inputboard(playerssetup,currplayer,inpposn,board)
        a=checkcurrplayerwonornot(playerssetup,currplayer,inpposn,board)
        from IPython.display import clear_output 
        clear_output()
        printboard(board)
        if a==True:
            print("PLAYER {} has WON".format(currplayer))
            return
        currplayer=swapcurrplayer(currplayer)
    print("The game has ended in a TIE.....")
status=True
while status:
    playtictactoe()
    inp=input("Do You want to play TIC TAC TOE again ?")
    if inp.lower()=='no':
        status=False
