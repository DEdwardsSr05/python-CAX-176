# Script to check user permissions 
# Binary as integers

READ = 4     # Binary 100
WRITE = 2    # Binary 010
EXECUTE = 1  # Binary 001

# Ask for surrent user permission
user_permission = int(input('What is current permission? Enter 1-7: '))  # Binary 010

print('*****Bitwise Testing*****')

if (user_permission & WRITE) == WRITE:
    print('Success, user has WRITE permission')

else:
    print('User does not have permission for WRITE')