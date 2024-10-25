from Cave import Cave
from Character import Enemy, Friend
from Item import Item
cavern = Cave('Cavern')
grotto = Cave('Grotto')
dungeon = Cave("Dungeon")
cavern.setdes('A damp and dirty cave')
grotto.setdes("A small cave with some ancient art")
dungeon.setdes('A large cave with a big gate')
cavern.linkcaves(dungeon, 'south')
cavern.linkcaves(grotto, 'south-west')
grotto.linkcaves(dungeon, 'east')
dungeon.linkcaves(grotto, 'west')
dungeon.linkcaves(cavern, 'north')
Harry = Enemy("Harry", "A smelly Wimpus")
Harry.setconvo("Hangry...Hanggrry")
Harry.setweak('Vegemite')
Josephine = Friend("Josephine", "A friendly bat")
Josephine.setconvo("Gidday")
grotto.setchar(Josephine)
dungeon.setchar(Harry)
vegemite = Item("Vegemite")
vegemite.setdes("A Wumpuses worst nightmare")
grotto.setitem(vegemite)
torch=Item("Torch")
torch.setdes("A light for the end of the tunnel")
dungeon.setitem(torch)
bag = []
currentcave = cavern
dead = False
while dead ==False:
    item = currentcave.getitem()
    if item is not None:
        item.describe()
    print('\n')
    currentcave.getlinks()
    inhabitant = currentcave.getchar()
    if inhabitant is not None:
        inhabitant.describe()
    command = input('>')
    if command in ['north', 'south', 'south-west', 'east', 'west']:
        currentcave = currentcave.move(command)
    elif command == 'talk':
        if inhabitant is not None:
            inhabitant.talk()
    elif command == 'fight':
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            weapon = input("What will you fight with? ")
            if weapon in bag:
                if inhabitant.fight(weapon) == True:
                    if Enemy.enemiestodefeat == 0:
                        print('congratulations, you have survived another andventure!')
                        dead = True
                    currentcave.setchar(None)
                    print('Bravo, hero you won the fight!')
                else:
                    print('Scurry home, you lost the fight.')
                    print("That's the end of the game")
                    dead = True
            else:
                print(f"You don't have a {weapon}")
        else:
            print('There is no one here to fight with')
    elif command == 'pat':
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.pat()
        else:
            print('There is no one here to pat :(')
    elif command == 'take':
        if item is not None:
            print(f"You put the {item.getname()} in your bag")
            bag.append(item.getname())
            currentcave.setitem(None)
    