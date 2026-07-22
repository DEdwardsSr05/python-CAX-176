# David Edwards
# 2026-CAX-176
# July 21, 2026
# ALAB 353.4
# basic_functions.py
# Defines and demonstrates three simple functions: greet_user, add_two_numbers, is_even

def greet_user(name=""):
    # Default parameter value "" means calling greet_user() with no argument won't error out
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")

def add_two_numbers(a, b):
    # return sends the value back to whoever called the function, unlike print()
    # which just displays it — return lets you store/reuse the result
    return a + b

def is_even(num):
    # % is modulo — if there's no remainder dividing by 2, the number is even
    return num % 2 == 0

# --- MAIN PROGRAM: demonstrate each function ---

greet_user("David")   # with a name
greet_user()          # without a name — falls back to default

sum_result = add_two_numbers(7, 5)
print(f"7 + 5 = {sum_result}")

print(f"4 is even: {is_even(4)}")
print(f"7 is even: {is_even(7)}")