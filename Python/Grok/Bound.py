#set the maximum group size and a minimum age
max_size = int(6)
min_age = int(18)
#Ask for the number of participants in the group. Max group size is 6 people.

group_size = int(input('How many people are in your group? '))

#check the input to see if the group size is between 1 and 6
#if the group size is within the limits, use a loop to get check how many bikes are needed.

if group_size <= 0:
  print('Group sizes must be between 1 and 6 people.')
elif group_size > max_size:
  print ('The maximum group size is 6 people.')
else:
  for i in range(group_size):
    name = input("Participant's name: ")
    age = int(input("Participant's age: "))
    if age < min_age:
      print(f'{name} is not old enough for this adventure.')
    else:
      print(f'Get ready to push your boundaries with this cycling adventure, {name}.')
         

