def Calc():
    print('Welcome to the calculator')
    print()
    print('Add = A')
    print('Subtract = S')
    print('Multiply = M')
    print('Divide = D')
    print()
    #ask for what function
    func=str(input('Please select what operation you would like to do: '))
    print()
    #if A (Add) is the functon variable
    if func =='A':
        def add():
            print('A+B=C')
            print()
            #ask for A and B
            a=int(input("A: "))
            b=int(input("B: "))
            #add A and B
            c = a + b
            #print full expression
            print(F'{a}+{b}={c}')
            print()
        add()
    #if S (Subtract) is the functon variable
    if func =='S':
        def subtract():
            print('A-B=C')
            print()
            #ask for A and B
            a=int(input("A: "))
            b=int(input("B: "))
            #subtract B from A
            c = a-b
            #print full expression
            print(F'{a}-{b}={c}')
            print()
        subtract()
    #if M (Multiply) is the functon variable
    if func =='M':
        def Multiply():
            print('AxB=C')
            print()
            #ask for A and B
            a=int(input("A: "))
            b=int(input("B: "))
            #multiply A and B together
            c = a*b
            #print full expression
            print(F'{a}x{b}={c}')
            print()
        Multiply()
    #if D (Divide) is the functon variable
    if func =='D':
        def divide():
            print('A/B=C')
            print()
            #ask for A and B
            a=int(input("A: "))
            b=int(input("B: "))
            #if B (divide by) = 0 then the result is impossible
            if b == 0:
                print("NaN")
            #if B is not 0 then the result is possible
            else:
                #divide A by D
                c = a/b
                #print full expression
                print(F'{a}/{b}={c}')
                print()
        divide()
    #Ask for retry
    print('Would you like to go again? (Y/N)')
    Retry = input("")
    #If Y (Yes) then rerun the program
    if Retry == "Y":
        Calc()
    #else quit
    else:
        quit()
Calc()