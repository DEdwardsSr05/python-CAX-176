#Greet people trying to enter the club
print("Welcome to City Lights, may I see your ID please?")

#Declare an age variable and assign a value
age = 35

#If the age is less than 35, print a message denying entry
print("please enter your age: ")
input_age = int(input('Enter your age: '))
if input_age < age:
    print("Sorry, you are not old enough to enter the club.")   
if input_age >= age:
    print("Welcome to the club! Enjoy your night!")


