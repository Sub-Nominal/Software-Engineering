print('Welcome to Tic Tac Toe')
#set win combinations
wincombo=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
player1list=[]
player2list=[]
print()
#get player names
player1 = input('Enter the name of Player 1: ')
player2 = input('Enter the name of Player 2: ')
print()
#set that the game isn't won and it is player 1's turns
NoWin = True
turn = 1
turncount = 0
#list the numbers on the board-
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#function to print the board
def Printboard():
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print('------------')
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print('------------')
    print(f" {board[6]} | {board[7]} | {board[8]}")
Printboard()
print()
#while there isnt a win
while NoWin and turncount <=8:
    #turn 1 is X's turn
    while turn==1 and NoWin:
        print('Hello', player1)
        turncount = turncount+1
        #ask for where the location of the cross will be
        Xloc = int(input('Where do you want to place the cross (1-9):'))
        while Xloc >=10 or Xloc <=0:
            print()
            print('Enter a number from 1-9!')
            print()
            Xloc = int(input('Where do you want to place the cross (1-9):'))
        if Xloc-1 in player2list:
            print()
            print('Choose a different space!')
            print()
            Xloc = int(input('Where do you want to place the nought (1-9):'))
        #subtracts 1 from xloc because the values of the locations are 1 higher then the board index and places an 'X' in place of the value
        board[Xloc-1]="X"
        winloc = Xloc-1
        #adds the location to player 1's list of locations
        player1list.append(winloc)
        player1list.sort()
        print(player1list)
        #check if player 1's list has any of the combinations in the sublists of the win combinations
        for sublist in wincombo:
            #if all elements in player 1's list are the same as a winning sublist then they win
            if all(elem in player1list for elem in sublist):
                print()
                print(f"{player1} wins!")
                NoWin=False
        print()
        Printboard()
        turn = 2
    #turn 2 is nought's turn
    while turn == 2 and NoWin:
        print('Hello', player2)
        turncount = turncount+1
        #ask for where the location of the nought will be
        Xloc = int(input('Where do you want to place the nought (1-9):'))
        while Xloc >=10 or Xloc <=0:
            print()
            print('Enter a number from 1-9!')
            print()
            Xloc = int(input('Where do you want to place the nought (1-9):'))
        if Xloc-1 in player1list:
            print()
            print('Choose a different space!')
            print()
            Xloc = int(input('Where do you want to place the nought (1-9):'))
        #subtracts 1 from xloc because the values of the locations are 1 higher then the board index and places an 'O' in place of the value
        board[Xloc-1]="O"
        winloc=Xloc-1
        #adds the location to player 2's list of locations
        player2list.append(winloc)
        player2list.sort()
        #check if player 1's list has any of the combinations in the sublists of the win combinations
        for sublist in wincombo:
            #if all elements in player 2's list are the same as a winning sublist then they win
            if all(elem in player2list for elem in sublist):
                print()
                print(f'{player2} wins!')
                NoWin=False
        print()
        Printboard()
        turn = 1
if NoWin == True and turncount > 7:
    print('Draw')