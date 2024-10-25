M = int(input("What is the Mass of the object: "))
if M < 1:
    print("Uh uh uh you didn't say the magic word")
    exit()
def Energy():
    C= 300000000
    e = M*C**2
    print(F'{e} Joules')
Energy()