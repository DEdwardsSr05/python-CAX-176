#Lab 351.2 - Simple Calculator
#David Edwards
#2026-CAX-176
#07-06-2026

#Take two numbers from the user and perform basic arithmetic operations on them.
#Get the first number from the user and convert it to a float.
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

#Ask user for desired operation
operation = input('Choose an operation to perform (+, -, *, /): ')

#Perform the operation based on user input
if operation == '+':
    result = num1 + num2
    print(f'The result of {num1} + {num2} is: {result}')
elif operation == '-':
    result = num1 - num2
    print(f'The result of {num1} - {num2} is: {result}')
elif operation == '*':
    result = num1 * num2
    print(f'The result of {num1} * {num2} is: {result}')
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f'The result of {num1} / {num2} is: {result}')
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid operation. Please choose +, -, *, or /.')