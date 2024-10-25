drink = input("WHAT DRINK DO YOU WANT TO ORDER? ")
if drink.upper() == drink:
    num = input("HOW MANY? ")
    print(f"{num} {drink}S COMING RIGHT UP!")

elif drink == drink.lower():
    print("I DIDN'T HEAR YOUR ORDER!")
else:
    print("I CAN'T UNDERSTAND YOU!")