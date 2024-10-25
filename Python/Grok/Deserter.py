DESSERT= {}
line = input('Name:Vote ')
while line:
    name, vote= line.split(':')
    if vote not in DESSERT:
        DESSERT[vote] = (name)
    else:
        DESSERT[vote].append(name)
        line = input('Name:Dessert')
for vote in DESSERT:
    print(vote, ' ', len(DESSERT[vote]), ' vote(s)', ' '.join(DESSERT[vote]))