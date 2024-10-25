def TrigCalc():
    #Get side lengths
    print()
    SideA = int(input('Lenght of Side A: '))
    SideB = int(input('Lenght of Side B: '))
    SideC = int(input('Lenght of Side C: '))
    print()
    if SideA !=0 and SideB !=0 and SideC !=0:
    #triangle equality check
        if SideA + SideB >= SideC and SideA + SideC >= SideB and SideB + SideC >= SideA:
            #if not right then it could be equal
                if SideA == SideB == SideC:
                    print('This triangle is Equilateral')
                    print()
                #if not equal or right then isoceles
                elif SideA == SideB != SideC or SideA == SideC != SideB or SideC == SideB != SideA:
                    print('This triangle is Isoceles')
                    print()
                #all sides inequal is scalene
                elif SideA != SideB != SideC and SideB != SideA != SideC and SideC != SideB != SideC:
                    print('This triangle is Scalene')
                    print()
                #pythagoras used because it only works for right triangles
                if SideA**2 + SideB**2 == SideC**2 or SideA**2 + SideC**2 == SideB**2 or SideB**2 + SideC**2 == SideA**2:
                    print('This Triangle is Right Angled')
                    print()
        else:
            #triangle inequality error
            print("The two smallest sides must be greater or equal to the largest side")
            #ask for retry
            rt = input("Would you like to input another triangle? Y/N ")
            #if yes then run trigcalc again
            if rt == 'y' or 'Y':    
                 TrigCalc()    
            #if no then quit
            elif rt == 'N' or 'n':
                quit()
    else:
        #zero length error
            print("Sides must be above 0")
            #ask for retry
            rt = input("Would you like to input another triangle? Y/N ")
            #if yes then run trigcalc again
            if rt == 'y' or 'Y':    
                 TrigCalc()    
            #if no then quit
            elif rt == 'N' or 'n':
                quit()
TrigCalc()