#ask the user for hours spent servicing bikes
time = float(input('Hours spent servicing bikes this week: '))

#check that time is a positive value
if time<=0:
  print("You should have done some work this week!")
else:  #ask for number of bikes serviced
  bikes_serviced = int(input('Bikes serviced this week: ')) 
  
#check that number of bikes is a positive value
  if bikes_serviced<=0:
    print("That's not good for business!")
  else:
    #calculate the average time spent per bike
    avg_time = time/bikes_serviced

    #round avg_time to one decimal place
    avg_time_rounded = avg_time.__round__(1)
    print(f'You spend approximately {avg_time_rounded} hours per bike.')

    #calculate weekly pay
    hourly_rate = 24.10
    weekly_pay = avg_time_rounded*hourly_rate*bikes_serviced 

    #round the weekly pay to the nearest dollar
    weekly_pay_rounded = weekly_pay.__round__()
    print(f'You will need to pay your helper approximately ${weekly_pay_rounded}.' )