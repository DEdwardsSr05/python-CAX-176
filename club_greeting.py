#Greet people trying to enter the club
print('Welcome to City Lights, may I see your ID please?')

#Declare an age variable and assign a value
age = int(input('Please enter your age: '))

#If the age is less than 18, print a message denying entry
if age < 18:
    print('I\'m sorry, but you\'re too young')

elif age <= 20:
    print('Here is a red armband. You can go inside, but not able to buy drinks.')

elif age > 27:
    print('Grown folk club down the road.')

else:
    print('Welcome in!! Enjoy your night.')

