def ui():
    print()
    print('Welcome to my Assesment Task 1')
    print("Please choose which program to run")
    print()
    print('1. Calculator, C')
    print('2. Triangle Identifier, TI')
    print('3. Tic Tac Toe, TT')
    print('4. Morse Code, M')
    print()
    #Data Structure-Set
    option1 = {"1", "Calculator", "calculator", "C", "c", "CALCULATOR"}
    option2 = {"2", "Triangle Identifier", "triangle identifier", "triangle Identifier", "TI", "ti", "Ti", "tI", "TRIANGLE IDENTIFIER"}
    option3 = {"3", "Tic Tac Toe", "tic tac toe", "Tic tac toe", "Tic Tac toe", "tic tac Toe", "tic Tac Toe", "TT", "tt", "Tt", "tT", "TIC TAC TOE"}
    option4 = {"4", "Morse Code", "morse code", "morse Code", "M", "m", "MORSE CODE"}
    #Sequence
    option = input("Please enter the Name, Number or Shorthand of the program you wish to run: ")
    print()
    #Selection
    if option in option1:
        #Subprogram
        def Calc():
            print('Welcome to the calculator')
            print('Please select which operation you would like to do')
            print()
            print('1. Add, A')
            print('2. Subtract, S')
            print('3. Multiply, M')
            print('4. Divide, D')
            #Data Structure-Set
            Option1c = {"Add", "add", "a", "A", "ADD", "1"}
            Option2c = {"Subtract", "subtract", "s", "S", "SUBTRACT", "2"}
            Option3c = {"Multiply", "multiply", "m", "M", "MULTIPLY", "3"}
            Option4c = {"Divide", "divide", "d", "D", "DIVIDE", "4"}
            print()
            #ask for what function
            func=str(input('Please enter the Name, Number or Shorthand for the operation you would like to do: '))
            print()
            #Selection
            if func in Option1c:
                def add():
                    print('A+B=C')
                    print()
                    #ask for A and B
                    a=float(input("A: "))
                    b=float(input("B: "))
                    #add A and B
                    c = a + b
                    #print full expression
                    print(F'{a}+{b}={c}')
                    print()
                add()
            #Selection
            if func in Option2c:
                def subtract():
                    print('A-B=C')
                    print()
                    #ask for A and B
                    a=float(input("A: "))
                    b=float(input("B: "))
                    #subtract B from A
                    c = a-b
                    #print full expression
                    print(F'{a}-{b}={c}')
                    print()
                subtract()
            #Selection
            if func in Option3c:
                def Multiply():
                    print('AxB=C')
                    print()
                    #ask for A and B
                    a=float(input("A: "))
                    b=float(input("B: "))
                    #multiply A and B together
                    c = a*b
                    #print full expression
                    print(F'{a}x{b}={c}')
                    print()
                Multiply()
            #Selection
            if func in Option4c:
                def divide():
                    print('A/B=C')
                    print()
                    #ask for A and B
                    a=float(input("A: "))
                    b=float(input("B: "))
                    #if B (divide by) = 0 then the result is impossible
                    if b == 0:
                        print("NaN")
                    #if B is not 0 then the result is possible
                    else:
                        #divide A by B
                        c = a/b
                        #print full expression
                        print(F'{a}/{b}={c}')
                        print()
                divide()
            else:
                print('Would you like to go again? (Y/N)')
            Retry = input("")
            #Iteration
            if Retry == "Y":
                Calc()
            #else quit
            else:
                re = input("Would you like to return to the menu? (Y/N) ")
                if re == "Y":
                    ui()
                else:
                    quit(ui)
            #Ask for retry
            print('Would you like to go again? (Y/N)')
            Retry = input("")
            #Iteration
            if Retry == "Y":
                Calc()
            #else quit
            else:
                re = input("Would you like to return to the menu? (Y/N) ")
                if re == "Y":
                    ui()
                else:
                    quit(ui)
        Calc()
    if option in option2:
        #Subprogram
        def TrigCalc():
            #Sequence
            print()
            SideA = float(input('Lenght of Side A: '))
            SideB = float(input('Lenght of Side B: '))
            SideC = float(input('Lenght of Side C: '))
            print()
            #Selection
            if SideA !=0 and SideB !=0 and SideC !=0:
            #Selection
                if SideA + SideB >= SideC and SideA + SideC >= SideB and SideB + SideC >= SideA:
                    #Selection
                        if SideA == SideB == SideC:
                            print('This triangle is Equilateral')
                            print()
                        #Selection
                        elif SideA == SideB != SideC or SideA == SideC != SideB or SideC == SideB != SideA:
                            print('This triangle is Isoceles')
                            print()
                        #Selection
                        elif SideA != SideB != SideC and SideB != SideA != SideC and SideC != SideB != SideC:
                            print('This triangle is Scalene')
                            print()
                        #Selection
                        if SideA**2 + SideB**2 == SideC**2 or SideA**2 + SideC**2 == SideB**2 or SideB**2 + SideC**2 == SideA**2:
                            print('This Triangle is Right Angled')
                            print()
                else:
                    print("The two smallest sides must be greater or equal to the largest side")
                    #Iteration
                    print()
                    rt = input("Would you like to input another triangle? Y/N ")
                    #Selection
                    if rt == 'Y':    
                        TrigCalc()    
                    #Selection
                    else:
                        re = input("Would you like to return to the menu? (Y/N) ")
                        if re == "Y":
                            ui()
                        else:
                            quit(ui)
            else:
                print("Sides must be above 0")
                #Iteration
                print()
                rt = input("Would you like to input another triangle? Y/N ")
                #Selection
                if rt =='Y':    
                    TrigCalc()    
                #Selection
                else:
                    re = input("Would you like to return to the menu? (Y/N) ")
                    if re == "Y":
                        ui()
                    else:
                        quit(ui)
            rt = input("Would you like to input another triangle? Y/N ")
            #Selection
            if rt =='Y':    
                TrigCalc()    
            #Selection
            else:
                re = input("Would you like to return to the menu? (Y/N) ")
                if re == "Y":
                    ui()
                else:
                    quit(ui)
        TrigCalc()    
    if option in option3:
        #Tic Tac Toe
        def TicTacToe():
            print('Welcome to Tic Tac Toe')
            #Data Structure-List
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
            #Data Structure-List
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
            #while there isnt a win #Selection
            while NoWin and turncount <=8:
                #turn 1 is X's turn #Selection
                while turn==1 and NoWin:
                    print('Hello', player1)
                    turncount = turncount+1
                    #ask for where the location of the cross will be
                    Xloc = int(input('Where do you want to place the cross (1-9): '))
                    #Selection
                    while Xloc >=10 or Xloc <=0:
                        print()
                        print('Enter a number from 1-9!')
                        print()
                        Xloc = int(input('Where do you want to place the cross (1-9): '))
                    #Selection
                    if Xloc-1 in player2list:
                        print()
                        print('Choose a different space!')
                        print()
                        Xloc = int(input('Where do you want to place the nought (1-9): '))
                    #subtracts 1 from xloc because the values of the locations are 1 higher then the board index and places an 'X' in place of the value
                    board[Xloc-1]="X"
                    winloc = Xloc-1
                    #adds the location to player 1's list of locations
                    player1list.append(winloc)
                    player1list.sort()
                    print(player1list)
                    #check if player 1's list has any of the combinations in the sublists of the win combinations
                    for sublist in wincombo: #Selection
                        #if all elements in player 1's list are the same as a winning sublist then they win
                        #Selection
                        if all(elem in player1list for elem in sublist):
                            print()
                            print(f"{player1} wins!")
                            NoWin=False
                            print()
                            ry = input('Would you like to play again? (Y/N) ')
                            if ry == "Y":
                                TicTacToe()
                            else:
                                re = input("Would you like to return to the menu? (Y/N) ")
                                if re == "Y":
                                    ui()
                                else:
                                    quit(ui)
                    print()
                    Printboard()
                    turn = 2
                #turn 2 is nought's turn
                #Selection
                while turn == 2 and NoWin:
                    print('Hello', player2)
                    turncount = turncount+1
                    #ask for where the location of the nought will be
                    Xloc = int(input('Where do you want to place the nought (1-9): '))
                    #Selection
                    while Xloc >=10 or Xloc <=0:
                        print()
                        print('Enter a number from 1-9!')
                        print()
                        Xloc = int(input('Where do you want to place the nought (1-9): '))
                    #Selection
                    if Xloc-1 in player1list:
                        print()
                        print('Choose a different space!')
                        print()
                        Xloc = int(input('Where do you want to place the nought (1-9): '))
                    #subtracts 1 from xloc because the values of the locations are 1 higher then the board index and places an 'O' in place of the value
                    board[Xloc-1]="O"
                    winloc=Xloc-1
                    #adds the location to player 2's list of locations
                    player2list.append(winloc)
                    player2list.sort()
                    #check if player 1's list has any of the combinations in the sublists of the win combinations
                    for sublist in wincombo: #Selection
                        #if all elements in player 2's list are the same as a winning sublist then they win
                        #Selection
                        if all(elem in player2list for elem in sublist):
                            print()
                            print(f'{player2} wins!')
                            NoWin=False
                            print()
                            ry = input('Would you like to play again? (Y/N) ')
                            if ry == "Y":
                                TicTacToe()
                            else:
                                re = input("Would you like to return to the menu? (Y/N) ")
                                if re == "Y":
                                    ui()
                                else:
                                    quit(ui)
                    Printboard()
                    turn = 1
            #Selection
            if NoWin == True and turncount > 7:
                print('Draw')
                ry = input('Would you like to play again? (Y/N) ')
                if ry == "Y":
                    TicTacToe()
                else:
                    re = input("Would you like to return to the menu? (Y/N) ")
                    if re == "Y":
                        ui()
                    else:
                        quit(ui)
        TicTacToe()
    if option in option4:
        def morsecode():
            #Data Structure-Dictionary
            Morsedictionary = { "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F":"..-.", "G":"--.", "H":"....", "I":"..","J":".---","K":"-.-","L":".-..","M":"--",
                                    "N":"-.", "O":"---", "P":".--.","Q":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..", "1":".----","2":"..---",
                                    "3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}
            def MorseEncode(message):
                morse_code = ''
                for char in message.upper():
                    #Slection
                    if char in Morsedictionary:
                        morse_code += Morsedictionary[char] +' '
                #Return
                return morse_code
            def MorseDecode(morse_code):
                message = ''
                morse_code = morse_code.split(' ')
                for code in morse_code:
                    #Selection
                    for char, morse in Morsedictionary.items():
                        if morse == code:
                            message += char
                #Return
                return message
            def main():
                choice = input("Would you like to decode or encode: ")
                #Data Structure-Set
                O1 = {"Encode", "ENCODE", "encode"}
                O2 = {"Decode", "DECODE", "decode"}
                #Selection
                if choice in O1:
                    print()
                    message = input("Enter a mesage to be encoded: ")
                    morse_code = MorseEncode(message)
                    print(morse_code)
                    #Selection
                if choice in O2:
                    print()
                    morse_code = input("Enter a morse code sequence to be decoded: ")
                    message = MorseDecode(morse_code)
                    print(message)
                #Selection
                if choice not in O1 and O2:
                    print('Please try again')
                    main()
                #Iteration
                ry = input('Would you like to go again? (Y/N) ')
                if ry == "Y":
                    main()
                else:
                    re = input("Would you like to return to the menu? (Y/N) ")
                    if re == "Y":
                        ui()
                    else:
                        quit(ui)
            main()
        morsecode()
    elif option not in option1 or option2 or option3 or option4:
        ui()
ui()
