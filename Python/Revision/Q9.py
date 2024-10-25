print("Username must be 8 characters or less. No numbers or symbols.")
un = input("Username: ")
if len(un)>8:
    print(f"Username is {len(un)-8} characters too long")
    lenv = False
else:
    lenv=True
if un.isalpha() == False:
    print(f"Username contains invalid symbols")
    lens = False
else:
    lens = True
if lenv == True and lens == True:
    print(f"Username is valid")
else:
    print(f"Username is invalid")