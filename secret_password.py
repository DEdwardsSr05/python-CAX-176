#Password script to count failures and alert when access granted

# sets up starting password value
password = ''   

# sets up starting attempts value of 0, has not tried a password yet
attempts = 0    

# one stopping rule, breaks if passowrd is correct or after three failures
while attempts < 3:   
    password = input('Enter password: ')
    if password == 'python123':
        print('Access granted')
        break
    else:
        print('Access denied')

    # counts attempts
    attempts = attempts + 1

# print access denied after 3 failed attempts
else:
    print('Account locked. Try again later')
