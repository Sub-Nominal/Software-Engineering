#getting user input on bicycle type 
mountain_bike = input("Do you have a mountain bike (yes/no)? " )
nein = {"No", "no", "NO", "nO"}
ja = {"Yes", "yes", "YES", "YeS", "yES", "yeS"}
#making a decision based on bicycle type
if mountain_bike in nein:
    print("Sorry, I can only fix up mountain bikes.")
elif mountain_bike in ja:
  first_name = input("Enter your first name: ")
  phone_num = input("Enter your contact phone number: ")
  print(f'Thank you, {first_name}. I will contact you on {phone_num} to schedule a fixer-up time!')
else:
  print("Invalid input.")