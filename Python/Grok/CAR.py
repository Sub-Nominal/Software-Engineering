carcolours = {}
while True:
    colour = input('Car: ')
    if not colour:
        break
    carcolours.setdefault(colour, 0)
    carcolours[colour] +=1
for colour, n in carcolours.items():
    print(f'Cars that are %s: %s' % (colour, n))