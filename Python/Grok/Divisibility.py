#This function will take in two integer numbers as arguments, a dividend and a divisor.
#Using modulo calculations, it will return whether the dividend is a multiple of the divisor.

def divisibility_checker(dividend, divisor):
        x = int(dividend%divisor)
        if x == 0:
            return True
        else:
            return False

#Write the rest of your program here
#Get user input for the dividend and divisor
divid = int(input("Enter an integer dividend: "))
divis = int(input("Enter an integer divisor: "))

#Determine if the dividend is a multiple of the divisor by calling the divisibility_checker function
yn =divisibility_checker(divid, divis)

#Print the result
if yn == True:
    print(f"{divid} is a multiple of {divis}")
else:
    print(f"{divid} is not a multiple of {divis}")
