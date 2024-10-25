favcol = {}
line = input('Name and colour: ')
while line:
    name, colour = line.split()
    favcol[name] = colour
    line = input('Name and colour: ')
for name in favcol:
    print(name, favcol[name])