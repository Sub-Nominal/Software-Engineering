#This function takes an integer as an argument - roll 
#and returns a food value based on the value of roll
def choose_delicacy(roll):
    if roll <=5:
        return "pizza"
    elif 6<= roll <=14:
        return "fish and chips"
    elif 15<= roll <=19:
        return "Chinese"
    elif roll == 20:
        return "Thai"

#Get input from the dice roll
d20 = int(input('What is the dice roll? '))

#Call the choose_delicacy function and save the value in a variable
delicacy = choose_delicacy(d20)

#Print out the results
print(f"You should order {delicacy}.")
