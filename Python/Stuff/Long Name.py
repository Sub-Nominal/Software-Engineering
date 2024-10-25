Name = input('Enter your name: ')
namelen = int(len(Name))
if namelen <=3:
    print(f'Hi {Name}, you have a short name.')
elif namelen <=8:
    print(f'Hi {Name}, nice to meet you.')
else:
    print(f'Hi {Name}, you have a long name.')