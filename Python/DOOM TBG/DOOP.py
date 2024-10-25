from Dudes import Enemy, Player
from LVL import Level
from Pickups import Pickup, AtkBoost
import time, math, random
import pygame
forward = ["Forward", "forward", "FORWARD"]
behind = ["Behind", "behind", "BEHIND"]
left = ["Left", "left", "LEFT"]
right = ["Right", "right", "RIGHT"]
E1M1 = Level(1, 1, "A facility on Mars... it seems abandoned", "E1M1")
E1M2 = Level(1, 2, "Deeper into the facility... no one is around", "E1M2")
E1M3 = Level(1, 3, "Even further into the facility... you hear screaming up ahead", "E1M3")
E1M4 = Level(1, 4, "The end of the facility... there seems to be something through the door", "E1M4")
E1M1.setmoves(E1M2, "forward")
E1M2.setmoves(E1M3, "forward")
E1M3.setmoves(E1M4, "forward")
hp1 = Pickup("Small Health Pack", "Heals a small amount of health", 5)
hp2 = Pickup("Medium Health Pack", "Heals a moderate amount of health", 10)
shotty = AtkBoost("Shotgun", "A simple shotgun, has better attack", 7)
E1M2.setpickup(hp1)
E1M3.setpickup(hp2)
E1M3.setpickup(shotty)
p = Player("Marine", "a marine stationed at a Mars base", 10, 5)
imp = Enemy("Imp", "A quick and nimble demon", 10, 2)
soldier = Enemy("Demon Soldier", "A demonic marine", 15, 5)
E1M3.setchar(imp)
E1M4.setchar(soldier)
print("\n")
currentlvl = E1M1
dead = False
while dead == False:
    currentlvl.describe()
    pickup = currentlvl.getpickup()
    if pickup is None:
        print("")
    elif pickup is not None:
        pickup.describe()
    print(" ")
    currentlvl.getmoves()
    command = input(">")