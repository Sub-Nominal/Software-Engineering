f = open('english.txt')
f = f.read().splitlines() 
f2 = open('french.txt')
f2 = f2.read().splitlines() 
for i in f:
    for l in f2:
        if i==l:
            print(i)