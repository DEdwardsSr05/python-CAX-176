# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.4
# calc_with_functions.py
# Refactors a basic calculator using separate functions per operation,
# plus a dispatcher function and exception handling for bad input.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b   # will raise ZeroDivisionError if b == 0 — handled by caller

def calculate(a, b, op):
    # Dispatcher: picks which operation function to call based on the symbol
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        print(f"Invalid operation: {op}")
        return None

# --- MAIN PROGRAM ---
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    result = calculate(num1, num2, operation)

    if result is not None:
        print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")